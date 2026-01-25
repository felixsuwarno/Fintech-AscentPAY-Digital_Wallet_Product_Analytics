import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Setup paths
script_dir = os.path.dirname(os.path.abspath(__file__))

# Project 05 structure:
# .py files live in /python
# CSV files live in /csv
data_dir = os.path.join(script_dir, "..", "csv")

users_path              = os.path.join(data_dir, "users.csv")
transactions_path       = os.path.join(data_dir, "transactions.csv")
events_path             = os.path.join(data_dir, "events.csv")
acquisition_costs_path  = os.path.join(data_dir, "acquisition_costs.csv")

# (Optional) normalize
users_path             = os.path.normpath(users_path)
transactions_path      = os.path.normpath(transactions_path)
events_path            = os.path.normpath(events_path)
acquisition_costs_path = os.path.normpath(acquisition_costs_path)

# 1. Pandas display settings
pd.set_option("display.max_columns", 200)
pd.set_option("display.max_rows", 100)
pd.set_option("display.width", 2000)

# 2. Load CSV files
df_users              = pd.read_csv(users_path)
df_transactions       = pd.read_csv(transactions_path)
df_events             = pd.read_csv(events_path)
df_acquisition_costs  = pd.read_csv(acquisition_costs_path)

# 3. Convert all dates to datetime objects (robust for mixed formats)
df_users["signup_ts"]               = pd.to_datetime(df_users["signup_ts"], format="mixed", errors="coerce").dt.normalize()
df_users["last_active_ts"]          = pd.to_datetime(df_users["last_active_ts"], format="mixed", errors="coerce").dt.normalize()
df_transactions["tx_ts"]            = pd.to_datetime(df_transactions["tx_ts"], format="mixed", errors="coerce").dt.normalize()
df_events["event_ts"]               = pd.to_datetime(df_events["event_ts"], format="mixed", errors="coerce").dt.normalize()
df_acquisition_costs["start_date"]  = pd.to_datetime(df_acquisition_costs["start_date"], format="mixed", errors="coerce").dt.normalize()
df_acquisition_costs["end_date"]    = pd.to_datetime(df_acquisition_costs["end_date"], format="mixed", errors="coerce").dt.normalize()

# ----------------- restrict cohort to 2024 signups only -----------------
cohort_start = pd.Timestamp("2024-01-01")
cohort_end   = pd.Timestamp("2025-01-01")  # half-open interval [2024-01-01, 2025-01-01)

df_users = df_users[(df_users["signup_ts"] >= cohort_start) & (df_users["signup_ts"] < cohort_end)].copy()

today           = df_transactions["tx_ts"].max()
delta180days    = pd.Timedelta(days=180)

# ----------------- find each user's 180 days LTV -----------------

# left join users and transactions table
df_user_tx = df_users.merge(df_transactions, on="user_id", how="left")

# prune columns we dont need
df_user_tx = df_user_tx[["user_id", "signup_ts", "tx_ts", "acquisition_channel", "revenue_to_app_usd", "is_refund"]]

# all users whose transaction is Null = transaction is now 0
df_user_tx["revenue_to_app_usd"]    = df_user_tx["revenue_to_app_usd"].fillna(0)
df_user_tx["is_refund"]             = df_user_tx["is_refund"].fillna(False)

# all refunded transactions will have its revenue_to_app_usd flipped, so that they will reduce summed revenue
df_user_tx.loc[df_user_tx["is_refund"] == True, "revenue_to_app_usd"] *= -1

# find users whose transaction dates are more than 180 days after signed up date
# OR
# users whose transaction date is done BEFORE their signup date.
# these users are now flagged in invalid_tx_mask
valid_tx_ts = df_user_tx["tx_ts"].notna()
invalid_tx_mask = valid_tx_ts & (
    (df_user_tx["tx_ts"] < df_user_tx["signup_ts"]) |
    ((df_user_tx["tx_ts"] - df_user_tx["signup_ts"]) > delta180days)
)

# for all users who are flagged as having invalid transactions, replace their revenue_to_app_usd with 0
df_user_tx.loc[invalid_tx_mask, "revenue_to_app_usd"] = 0

# group by user_id and sum revenue_to_app_usd to get LTV per user.
df_user_tx = (
    df_user_tx.groupby(["user_id", "acquisition_channel"], as_index=False)
    .agg(total_revenue=("revenue_to_app_usd", "sum"))
)

# Sort by total_revenue, and reset the index, make it start from 0 and up
df_user_tx = df_user_tx.sort_values(by="total_revenue", ascending=False).reset_index(drop=True)

# Create “pareto volume” (non-negative only)
df_user_tx["pareto_revenue"] = df_user_tx["total_revenue"].clip(lower=0)

# Cumulative revenue should use pareto_revenue
df_user_tx["cumulative_revenue"] = df_user_tx["pareto_revenue"].cumsum()

# Total revenue denominator should use pareto_revenue
total_rev = df_user_tx["pareto_revenue"].sum()

df_user_tx["cum_users"]     = df_user_tx.index + 1
df_user_tx["cum_users_pct"] = df_user_tx["cum_users"] / len(df_user_tx)
df_user_tx["cum_rev_pct"]   = df_user_tx["cumulative_revenue"] / total_rev

print(df_user_tx.head(100))

# Top X% revenue share (Pareto volume)
top_1_pct_users  = int(np.ceil(0.01 * len(df_user_tx)))
top_5_pct_users  = int(np.ceil(0.05 * len(df_user_tx)))
top_10_pct_users = int(np.ceil(0.10 * len(df_user_tx)))
top_20_pct_users = int(np.ceil(0.20 * len(df_user_tx)))

top_1  = df_user_tx.loc[df_user_tx.index <  top_1_pct_users, "pareto_revenue"].sum() / total_rev if total_rev > 0 else 0
top_5  = df_user_tx.loc[df_user_tx.index <  top_5_pct_users, "pareto_revenue"].sum() / total_rev if total_rev > 0 else 0
top_10 = df_user_tx.loc[df_user_tx.index < top_10_pct_users, "pareto_revenue"].sum() / total_rev if total_rev > 0 else 0
top_20 = df_user_tx.loc[df_user_tx.index < top_20_pct_users, "pareto_revenue"].sum() / total_rev if total_rev > 0 else 0

print(f"Top  1% revenue share :  {top_1:.2%}")
print(f"Top  5% revenue share :  {top_5:.2%}")
print(f"Top 10% revenue share : {top_10:.2%}")
print(f"Top 20% revenue share : {top_20:.2%}")

output_path = os.path.join(script_dir, "..", "csv", "06_pareto_ltv_180d.csv")
df_user_tx.to_csv(output_path, index=False)

# ================= Pareto Curve Visualization (Matplotlib) =================

# X and Y for Pareto curve
x = df_user_tx["cum_users_pct"].values
y = df_user_tx["cum_rev_pct"].values

plt.figure(figsize=(12, 8))

# ---------------- Pareto curve ----------------
plt.plot(
    x,
    y,
    linewidth=3,
    label="Pareto curve (Revenue)",
    zorder=3
)

# ---------------- Equal distribution line ----------------
plt.plot(
    [0, 1],
    [0, 1],
    linestyle="--",
    linewidth=1.5,
    alpha=0.7,
    label="Equal distribution",
    zorder=1
)

# ---------------- Highlight key percentiles ----------------
percentiles = [0.01, 0.05, 0.10, 0.20]

for p in percentiles:
    idx = int(np.ceil(p * len(df_user_tx))) - 1
    idx = max(idx, 0)

    x_p = x[idx]
    y_p = y[idx]

    # Dot at intersection
    plt.scatter(
        x_p,
        y_p,
        s=50,
        zorder=5
    )

    # Horizontal dotted line (Y-axis → dot)
    plt.hlines(
        y=y_p,
        xmin=0,
        xmax=x_p,
        linestyles=":",
        linewidth=1.5,
        alpha=0.9
    )

    # Vertical dotted line (X-axis → dot)
    plt.vlines(
        x=x_p,
        ymin=0,
        ymax=y_p,
        linestyles=":",
        linewidth=1.5,
        alpha=0.9
    )

    # Label (always to the RIGHT of the dot)
    label = f"{int(p*100)}% users  {y_p:.1%} revenue"
    plt.annotate(
        label,
        xy=(x_p, y_p),
        xytext=(10, 0),
        textcoords="offset points",
        ha="left",
        va="center",
        fontsize=12
    )

# ---------------- Axis limits ----------------
plt.xlim(0, 1)
plt.ylim(0, 1.10)

# ---------------- Axis labels ----------------
plt.xlabel(
    "Cumulative share of users",
    fontsize=14,
    labelpad=12
)

plt.ylabel(
    "Cumulative share of revenue",
    fontsize=14,
    labelpad=12
)

# ---------------- Axis ticks (20% increments, percent format) ----------------
plt.xticks(
    [0, 0.2, 0.4, 0.6, 0.8, 1.0],
    fontsize=12
)

plt.yticks(
    [0, 0.2, 0.4, 0.6, 0.8, 1.0],
    fontsize=12
)

plt.gca().xaxis.set_major_formatter(mtick.PercentFormatter(1.0))
plt.gca().yaxis.set_major_formatter(mtick.PercentFormatter(1.0))

# ---------------- Title ----------------
plt.title(
    "AscentPAY — Revenue Pareto Curve\n(2024 Signup Cohort, LTV 180 Days)",
    fontsize=18,
    pad=18
)

# ---------------- Legend ----------------
plt.legend(fontsize=12)

# ---------------- Clean look ----------------
plt.grid(False)
plt.tight_layout()
plt.show()