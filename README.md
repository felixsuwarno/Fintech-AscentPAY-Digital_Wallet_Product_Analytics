# WIP ( Jan 20 2026 )

# FinTech “AscentPAY” Digital Wallet Product Analytics  
**Activation • Retention • LTV • Revenue Concentration**

This project analyzes synthetic but realistic digital wallet data from AscentPAY, a simulated FinTech product designed to mirror real-world payment apps that monetize via net transaction revenue. 

The dataset includes tens of thousands of users, hundreds of thousands of transactions, and multiple supporting tables (users, transactions, events, and acquisition costs). 

The analysis evaluates user activation, retention, reactivation, customer value (LTV), unit economics, and revenue concentration using defensible, business-aligned metrics to assess overall product health and sustainability.

<br>

➤ **Project Goal / Purpose:**  
Evaluate whether AscentPAY’s revenue is driven by broad healthy usage or a small set of high-value users, and quantify sustainability via activation, retention, LTV, and CAC payback.

<br>

➤ **Skills Demonstrated:**  
Activation & engagement analytics, retention and reactivation analysis, cohort LTV modeling, monetization and revenue stack analysis, CAC efficiency and payback analysis, revenue concentration and Pareto analysis.
(SQL • Python • Pandas • fintech KPI design • executive storytelling )

<br>

➤ **Core Business Questions:**
- How long does it take users to complete their first revenue-generating transaction after signup?
- Do users return and transact consistently month-over-month?
- Is churn permanent, or can users be reactivated?
- Who actually generates revenue, and how concentrated is that value?
- Do users generate enough lifetime value to justify their acquisition cost?
- How fragile is revenue if the top revenue-contributing users churn (revenue concentration risk)?

<br>

➤ **Key Findings:**
( FOR LATER )

<br>

➤ **Core Issue Identified:**
( FOR LATER )

<br>

➤ **Executive Outcome:**  
( FOR LATER )

<br><br>

# ➤ The Main Report : 
---

<br>

## Dataset :

The raw dataset spans 2024–mid-2026, but this project’s reporting and conclusions are intentionally scoped to calendar year 2024. 

The analysis uses four core tables representing a digital wallet product:

**users**
  - One row per user
  - Contains signup timestamp, acquisition channel, device type, KYC level, risk segment, and demographics
  - Used to define cohorts and user-level attributes

**transactions**
  - One row per transaction
  - Includes transaction timestamp, transaction type, gross amount, net revenue to the app, and refund indicators
  - Used for activation, retention, revenue, LTV, and concentration analysis

**events**
  - One row per product event (e.g., app opens)
  - Used to measure product engagement and usage frequency (e.g., stickiness)

**acquisition_costs**
  - One row per acquisition channel and date range
  - Contains customer acquisition cost (CAC) assumptions by channel
  - Used to evaluate LTV-to-CAC efficiency and payback periods

The raw dataset spans **2024 through mid-2026**.  
All reporting and conclusions in this project are intentionally scoped to **calendar year 2024** for consistency.

<br>
---
<br>

# Key Questions Answered

## 1 - Activation & Engagement

<br>

**1.1 - User Activation Speed** <br>
How long does it take users to complete their first transaction after signup, and does activation speed differ by acquisition channel?

<p align="center">
  <img src="images/01_1_Average_User_Activation_Time_Interval.png" width="85%">
</p>

**Method**
- Identify users who made at least one transaction after signup
- For each of those users, find the date of their first transaction
- Calculate the number of days between signup and first transaction
- Average this time by acquisition channel
- Restrict the analysis to users who signed up in 2024

**Key Insights**
- Users acquired through employer partnerships activate the fastest, reaching their first transaction in under two weeks on average.
- Referral users activate relatively quickly, suggesting trust and intent accelerate early usage.
- Organic users take meaningfully longer to activate, indicating weaker initial intent or higher onboarding friction.
- Paid acquisition users are the slowest to activate by a wide margin, taking more than a month on average to complete their first transaction.
- Slower activation delays revenue realization and increases early churn risk, especially for paid acquisition channels.

<br>

**1.2 - Product Engagement (Monthly Stickiness)** <br>
Once users are active, how consistently do they return and use the product over time?

<p align="center">
  <img src="images/01_2_monthly_stickiness_ratio.png" width="85%">
</p>

**Method**
- Treat any transaction or in-app event as product activity
- Count daily active users (DAU) for each day
- Average daily active users within each month
- Count monthly active users (MAU) as distinct users per month
- Calculate monthly stickiness as average DAU divided by MAU
- Restrict the analysis to calendar year 2024

**Key Insights**
- Only a small share of monthly users use the product on a typical day.
- Stickiness increases early in the year, then levels off with a slight decline.
- Even at its peak, fewer than one in five monthly users are active daily.
- Daily usage remains limited relative to the overall monthly user base.

<br>

**1.3 - Business Implications** <br>

- Users make a first transaction, but most do not use the product often after that, so the business should focus on what users do after their first transaction.
- Users reach their first transaction quickly, but they do not come back many times, so the first transaction should be treated as the start, not the end.
- Making users activate faster does not make them use the product more often, so success should not be measured only by activation speed.
- Many users use the product only a few days in a month, so the product needs clearer reasons for users to come back more often.
- Improving activation speed alone will not change how often users use the product, so effort should be split between faster activation and more frequent use.

<br><br>


## 2 - Retention, Churn & Reactivation

**2.1 - Month-over-Month Retention & Churn (Revenue-Active Users)** <br>
What are the month-over-month retention and churn rates for revenue-active users?

<p align="center">
  <img src="images/02_1_MOM_churn_and_retention_rate.png" width="85%">
</p>

#### Method
- Treat user activity as having at least one transaction in a month
- Identify users with transactions in each calendar month of 2024
- A user is retained if they transact in two consecutive months
- Calculate month-over-month retention as retained users divided by prior-month active users
- Calculate month-over-month churn as users active in the prior month who do not transact again in the current month

#### Key Insights
- Early in the year, most revenue-active users continue transacting month to month, but from mid-year onward more users stop transacting between consecutive months.
- By late 2024, about 1 out of every 4 revenue-active users stops transacting each month.
- Over time, the level of churn increases and more users stop transacting.

<br>

**2.2 - Reactivation of Lapsed Users** <br>
When Users stop transacting, how often do they return and generate revenue again?

<p align="center">
  <img src="images/02_2_MOM_reactivation_rate.png" width="85%">
</p>

#### Method
- Identify users with at least one transaction in each month of 2024
- Build a universe of users who transacted at least once during 2024
- Classify users as:
  - **Retained**: transacted in both the current and previous month
  - **Reactivated**: transacted in the current month but not in the previous
- Calculate reactivation rate as reactivated users divided by users who were inactive in the prior month
- Track reactivation patterns across the year

#### Key Insights
Reactivation rates increases through mid-year, peaking around 25–27%, then decline toward the end of 2024.

<br>

**2.3 - Business Implications** <br>
- More users stop transacting month to month as the year goes on, and reactivation does not increase enough to compensate, so the active user base naturally shrinks over time.
- Although some users return after being inactive, this behavior weakens later in the year, so reactivation cannot be relied on to offset rising churn.
- Because fewer users stay active and fewer return after dropping out, maintaining revenue increasingly depends on keeping existing users from leaving in the first place.
- Efforts should focus more on preventing users from stopping their activity than on trying to bring them back after they leave.

<br><br>

## 3 - Customer Value (LTV)

**3.1- 180-day LTV by Signup Cohort** <br>
How much net revenue do users generate in their first 180 days by signup cohort?

<p align="center">
  <img src="images/03_1_cohort_ltv_180d.png" width="85%">
</p>

#### Method
- Restrict the analysis to users who signed up in 2024
- For each user, sum net revenue generated within the first 180 days after signup, treating refunds as negative revenue
- Ignore transactions that occurred before signup or after the 180-day window
- Aggregate total 180-day revenue by signup month
- Include all users, including those with zero revenue, to avoid survivorship bias
- Report total 180-day revenue per signup cohort and the share of users with LTV greater than zero

#### Key Insights
- Signup cohorts from earlier in 2024 generate more total revenue in their first 180 days than cohorts that joined later in the year.
- Total 180-day revenue declines for cohorts that sign up after mid-year.

<br>

**3.2- Early LTV by Acquisition Channel** <br>
Which signup sources produce users who generate the most value in their first 180 days?

<p align="center">
  <img src="images/03_2_cohort_ltv_180d_per_acquisition_channel.png" width="85%">
</p>

#### Method
- Start from all users and their signup date and acquisition channel.
- Join transactions to users so users with no transactions are still included.
- Count transaction revenue only if it happens within 180 days after signup.
- Treat refunds as negative revenue.
- Sum 180-day revenue at the user level.
- Aggregate results by signup month and acquisition channel, reporting cohort size and total 180-day revenue.
- The report is filtered to show only 2024 signup cohorts in Tableau; the SQL itself is not restricted to 2024.

#### Key Insights
- Organic cohorts generate the highest total 180-day revenue in most months (it leads in 10 out of 12 signup months).
- Employer_partner is usually second, and is #1 only in May and June.
- Referral is consistently strong but generally below organic and employer_partner (often #3, and #2 in a few late-year months).
- Paid_ads is the lowest 180-day revenue channel every month.
- Across all channels, 180-day revenue is much higher in the first half of 2024 than in the second half (later signup cohorts generate less total 180-day revenue than early cohorts).

<br>

**3.3 - Business Implications** <br>
- Total 180-day revenue falls for later signup cohorts mainly because there are fewer users, so the business needs to understand and address the decline in cohort size before expecting revenue to grow.
- Employer partner and referral channels generate more revenue per user within 180 days, so these channels should be treated as high-efficiency sources and protected from quality dilution.
- Paid acquisition generates the lowest 180-day revenue, so spending on this channel should be limited unless early revenue improves.
- Organic acquisition contributes the most total 180-day revenue but weakens for later cohorts, so relying on organic growth alone will not sustain revenue if cohort size continues to shrink.
- Because some channels generate revenue through volume and others through higher value per user, the business must decide which model it wants to scale and manage acquisition channels differently instead of treating them the same.

<br><br>

## 4 - Monetization Mechanics

**4.1- Overall Revenue Stack (GMV, Net Revenue, Take Rate)** <br>
How much transaction volume flows through the product, how much revenue AscentPAY captures, and how efficiently it monetizes that volume?

<p align="center">
  <img src="images/04_1_ revenue_stack_total.png" width="85%">
</p>

#### Method
- Restrict transactions to monetizable spend types (card payments, bill pay, FX payments).
- Exclude refunds from all calculations.
- Exclude top-ups and peer-to-peer transfers from GMV.
- Aggregate monthly GMV and net revenue.
- Compute take rate as net revenue divided by GMV.
- Filter the final report to calendar year 2024 in Tableau (not in the SQL).

#### Key Insights
- Net revenue rises through July, then declines through year-end.
- Take rate stays tightly stable (~1.18%–1.30%) month to month.

<br>

**4.2- Revenue Mix by Transaction Channel** <br>
Which transaction channel contribute most to revenue, and how their contribution changes over time?

<p align="center">
  <img src="images/04_2b_ revenue_stack_per_channel_1.png" width="85%">
</p>

<p align="center">
  <img src="images/04_2b_ revenue_stack_per_channel_2.png" width="85%">
</p>

#### Method
- Group transactions by month and transaction type (tx_type).
- Exclude refunds.
- Exclude top-ups and P2P sends from the analysis.
- Aggregate monthly GMV and net revenue for each transaction type.
- Compute take rate as net revenue ÷ GMV per transaction type.
- Restrict the analysis to calendar year 2024 (in SQL).

#### Key Insights
- Bill pay and card payments generate most of the net revenue throughout the year.
- Withdrawals contribute a smaller share of net revenue compared to bill pay and card payments.
- The share of revenue by transaction type stays similar month to month.
- No transaction type shows a sharp increase or decrease relative to the others

<br>

**4.3 - Business Implications** <br>
- Pricing and fees do not change over time, so revenue decreases when usage decreases and increases when usage increases.
- Bill pay and card payments generate most of the revenue, so changes in these two activities have the largest effect on total revenue.
- No transaction type grows faster than the others, so there is no transaction type that compensates when another one slows down.
- Overall, revenue closely follows how much users transact.

<br><br>

## 5 - Acquisition Efficiency

**5.1 - LTV vs CAC by Acquisition Channel** <br>
Do customers generate enough lifetime value within 180 days to cover their acquisition cost?

<p align="center">
  <img src="images/05_1_LTV_to_CAC_ratio.png" width="85%">
</p>

#### Method
- Calculate each user’s net revenue within 180 days of signup
- Aggregate 180-day LTV by acquisition channel
- Assign customer acquisition cost (CAC) to users based on acquisition channel and signup date
- Aggregate CAC by acquisition channel, excluding users without a matching CAC record
- Compute the channel-level LTV-to-CAC ratio as aggregated 180-day LTV divided by aggregated CAC
- Ratios above 100% indicate that, on average, the channel recovers acquisition cost within 180 days

#### Key Insights
- Referral users fully recover acquisition cost within 180 days (≈106%), making this the most efficient channel in this comparison.
- Employer partnerships recover a large share of CAC (≈74%) but do not fully pay back within 180 days.
- Paid ads recover only a small portion of CAC within 180 days (≈12%).
- Organic acquisition is excluded from the LTV-to-CAC comparison due to missing CAC attribution.
- Large differences in LTV-to-CAC ratios highlight wide variation in acquisition efficiency across channels.

<br>

**5.2 - CAC Payback Period by Acquisition Channel** <br>
How quickly does each acquisition channel generate enough revenue to repay its upfront acquisition cost?

<p align="center">
  <img src="images/05_2_CAC_payback_period.png" width="85%">
</p>

#### Method
- Calculate cumulative net revenue per user after signup
- Compare cumulative revenue to assigned CAC at fixed time windows (30, 60, 90, and 180 days)
- Determine whether each user has recovered CAC by each time window
- Calculate the share of users who recover CAC by each time window
- Report results by acquisition channel

#### Key Insights
- Referral users have the highest share of CAC recovery by 180 days (≈31%).
- Employer partner users recover CAC less often than referrals, with a moderate recovery rate by 180 days (≈24%).
- Paid ads have the lowest CAC recovery, with only a small share of users recovering CAC by 180 days (≈3%).
- Most users acquired through paid ads do not recover CAC within 180 days.

<br>

**5.3 - Business Implications** <br>
- Referral is the only channel that recovers acquisition cost within 180 days and has the highest share of users repaying CAC.
- Employer partnerships recover a meaningful portion of CAC but do not fully pay back within 180 days for most users.
- Paid acquisition performs poorly on both LTV/CAC and CAC recovery probability, with very few users repaying acquisition cost within 180 days.
- Channel efficiency differs not only in average LTV/CAC but also in how many users actually repay CAC, meaning averages alone can hide risk.


<br><br>

## 6 - Revenue Concentration & Risk

**6.1 - Revenue Skew from Extreme Users (IQR Analysis)** <br>
Do a small number of users disproportionately influence total revenue outcomes?

<p align="center">
  <img src="images/06_1_IQR_revenue_outliers.png" width="85%">
</p>

#### Method
- Aggregate **total net revenue per user** across all 2024 transactions
- Include refunds as negative revenue to reflect true net contribution
- Rank users by total net revenue
- Segment users into percentile-based buckets:
  - Top 1%, 5%, 10%, 20%
  - Middle 60%
  - Bottom 20%, 10%, 5%, 1%
- Compare **user count**, **average revenue per user**, and **total revenue** by bucket

#### Key Insights
- Revenue is **heavily skewed toward the top user segments**, with the top 20% contributing the majority of net revenue.
- The **middle 60% of users generate low average revenue**, despite representing the largest share of the user base.
- Bottom-percentile users contribute **negligible revenue**, indicating limited monetization depth across most users.
- Business performance is **highly sensitive to the behavior of a small set of high-value users**, increasing revenue volatility risk.

#### **Business Implications**
- Revenue concentration increases volatility and exposure to top-user churn.
- Most users contribute limited value, constraining broad-based monetization.
- Business outcomes depend heavily on retaining a small high-value segment.
- Protective strategies for power users are critical to revenue stability.

<br>

**6.2 - Revenue Concentration Across Users (Pareto Analysis)** <br>
What share of total revenue is driven by the top X% of users?

<p align="center">
  <img src="images/06_2_pareto_ltv_180d.png" width="85%">
</p>

#### Method
- Restrict analysis to **2024 signup cohort**
- Calculate each user’s **180-day net LTV** (refunds included)
- Sort users by revenue contribution (descending)
- Compute cumulative:
  - Percentage of users
  - Percentage of total revenue
- Plot Pareto curve and benchmark against equal distribution

#### Key Insights
- The **top 1% of users generate ~14% of total revenue**.
- The **top 5% generate ~43%**, and the **top 10% generate ~63%** of revenue.
- The **top 20% of users account for ~85% of total revenue**, confirming a strong Pareto effect.
- Revenue sustainability depends disproportionately on a **small fraction of power users**, creating concentration and churn risk at the top end.

#### **Business Implications**
- A strong Pareto effect confirms dependence on a small fraction of users.
- Losing a small number of top users can materially impact revenue.
- Growth strategies must balance power-user retention with broader monetization.
- Reducing concentration risk improves predictability and long-term resilience.

<br>

## 7 - Executive Recommendations & Strategic Focus
<br>

Based on the data, AscentPAY’s main problem is that revenue does not last over time and depends too much on a small group of users. The recommendations below focus on the changes that would have the biggest impact on the business.

**1. Rebalance Growth Away from Paid Acquisition**

- Users acquired through paid ads take the longest to activate, generate the lowest early value, and rarely recover their acquisition cost. As a result, scaling paid acquisition under current conditions increases churn and wastes capital.
- Growth effort should shift toward referral and employer partnership channels, which consistently produce higher-value users.

**2. Treat Retention as the Main Growth Problem**

- Users activate quickly, but many stop using the product after a few months.
- Too many users leave each month, which makes revenue unstable.
- Improving the experience after the first transaction is more effective than acquiring more users.

**3. Protect and Focus on High-Value Users**

- Most revenue comes from a small group of users.
- Losing these users would significantly reduce revenue.
- Retention efforts should focus on keeping these high-value users active.

**4. Do Not Rely on Reactivation as a Growth Strategy**
- Some users return after leaving, but most do not stay active for long.
- Many users use the product only when they need it, not regularly.
- It is better to keep users from leaving than to try to bring them back.

**5. Keep Pricing Stable and Increase Usage**
- Prices and fees are already stable and working as expected.
- Revenue grows mainly when users make more transactions.
- The product should focus on getting users to use it more often, not on changing prices.

**Strategic Focus Going Forward**
To grow in a healthy way, AscentPAY should focus on keeping users active, spending acquisition budget more carefully, and reducing dependence on a small group of users. Without fixing churn and revenue concentration, adding more users will increase risk instead of long-term growth.

