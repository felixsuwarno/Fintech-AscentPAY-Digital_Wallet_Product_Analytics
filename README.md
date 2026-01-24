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
- Identify each user’s first transaction timestamp after signup
- Calculate the number of days from signup to first transaction
- Average activation time by acquisition channel
- Restrict analysis to 2024 signup cohort

**Key Insights**
- Users acquired through employer partnerships activate the fastest, reaching their first transaction in under two weeks on average.
- Referral users activate relatively quickly, suggesting trust and intent accelerate early usage.
- Organic users take meaningfully longer to activate, indicating weaker initial intent or higher onboarding friction.
- Paid acquisition users are the slowest to activate by a wide margin, taking nearly a month on average to complete their first transaction.
- Slower activation delays revenue realization and increases early churn risk, especially for paid acquisition channels.

#### **Business Implications**
- Faster activation from employer partners and referrals shortens time-to-revenue and lowers early churn risk.
- Slow activation among paid users delays monetization and weakens CAC payback economics.
- Activation speed should be treated as a leading KPI for downstream retention and LTV.
- Improving onboarding for slow-activating channels offers higher ROI than increasing acquisition spend.

<br>

**1.2 - Product Engagement (Monthly Stickiness)** <br>
Once users are active, how consistently do they return and use the product over time?

<p align="center">
  <img src="images/01_2_monthly_stickiness_ratio.png" width="85%">
</p>

**Method**
- Define product activity as any transaction or in-app event
- Compute monthly DAU and MAU for 2024
- Calculate monthly stickiness as Avg DAU / MAU
- Track stickiness trends across the calendar year

**Key Insights**
- Product stickiness starts low early in the year, then rises quickly as the user base stabilizes.
- After the initial ramp-up, stickiness remains relatively flat throughout most of the year.
- The stable but modest stickiness level suggests habit formation without increasing usage intensity.
- Engagement does not compound over time, indicating limited natural growth from returning users alone.

#### **Business Implications**
- Stable but flat stickiness indicates habit formation without increasing usage depth.
- Engagement does not compound organically, limiting revenue growth from the existing base.
- Long-term growth cannot rely on engagement alone and requires either retention or acquisition improvements.
- Product investments should focus on increasing transaction frequency, not just maintaining baseline activity.

<br><br>


## 2 - Retention, Churn & Reactivation

**2.1 - Month-over-Month Retention & Churn (Revenue-Active Users)** <br>
What are the month-over-month retention and churn rates for revenue-active users?

<p align="center">
  <img src="images/02_1_MOM_churn_and_retention_rate.png" width="85%">
</p>

#### Method
- Define activity strictly as **revenue-generating transactions**
- Identify users active in each calendar month of 2024
- A user is **retained** if they transact in consecutive months
- Month-over-month retention = retained users ÷ prior-month active users
- Month-over-month churn = 1 − retention rate

#### Key Insights
- Early in the year, retention is extremely high (≈95–96%), indicating strong short-term continuation after first use.
- Starting mid-year, churn accelerates sharply, with retention falling into the low–mid 70% range.
- By late 2024, roughly **1 in 4 revenue-active users churn each month**, signaling structural retention weakness.
- The pattern suggests initial product adoption is strong, but sustained month-over-month value is not being delivered to a large portion of users.
- Revenue stability increasingly depends on a shrinking base of repeat users rather than broad ongoing engagement.

#### **Business Implications**
- High early retention masks structural churn that emerges later in the user lifecycle.
- Rising churn materially weakens revenue predictability and forecasting accuracy.
- Growth strategies that emphasize activation without retention reinforcement will plateau.
- Retention improvements yield outsized impact compared to acquisition at current churn levels.

<br>

**2.2 - Reactivation of Lapsed Users** <br>
When Users stop transacting, how often do they return and generate revenue again?

<p align="center">
  <img src="images/02_2_MOM_reactivation_rate.png" width="85%">
</p>

#### Method
- Identify users with revenue-generating transactions in each month of 2024
- Classify users as:
  - **Retained**: active in both current and previous month
  - **Reactivated**: active this month but inactive in the prior month
- Reactivation rate = reactivated users ÷ users inactive in the prior month
- Measure reactivation trends across the year

#### Key Insights
- Reactivation rises steadily through mid-year, peaking around **25–27%**, indicating some success in bringing lapsed users back.
- After the peak, reactivation declines toward year-end, suggesting diminishing effectiveness of organic return behavior.
- While reactivation partially offsets churn, it is **not sufficient to counteract rising monthly churn rates**.
- The product relies more on reacquiring previously active users than on retaining them continuously.
- This pattern points to episodic usage rather than durable habit formation.

#### **Business Implications**
- Reactivation helps recover some lost revenue but does not replace durable retention.
- Dependence on reactivation signals episodic rather than habitual product usage.
- As reactivation declines, churn increasingly translates into permanent revenue loss.
- Product and lifecycle efforts should prioritize preventing churn rather than relying on recovery.

  
<br><br>

## 3 - Customer Value (LTV)

**3.1- 180-day LTV by Signup Cohort** <br>
How much net revenue do users generate in their first 180 days by signup cohort?

<p align="center">
  <img src="images/03_1_cohort_ltv_180d.png" width="85%">
</p>

#### Method
- Restrict analysis to users who signed up in 2024
- Track each user’s net revenue during the first 180 days after signup
- Aggregate total 180-day net revenue by signup month
- Include all users, including those with zero revenue, to avoid survivorship bias
- Report total 180-day revenue per signup cohort and the share of users who generated any revenue

#### Key Insights
- Earlier 2024 signup cohorts generate meaningfully higher 180-day LTV than cohorts acquired later in the year.
- Peak cohort value occurs in Q1–Q2, followed by a steady decline for cohorts acquired after mid-year.
- The percentage of monetized users remains relatively stable across cohorts, indicating that **LTV decline is driven by lower per-user value**, not fewer paying users.
- Later cohorts monetize, but at materially lower intensity, suggesting weakening user quality or product value realization over time.
- This pattern indicates early growth cohorts benefited from stronger engagement or higher-value use cases that were not sustained later in the year.

#### **Business Implications**
- Declining cohort LTV over time indicates deteriorating user quality or value realization.
- Stable monetization rates suggest the issue is revenue depth, not conversion to paying users.
- Growth cohorts from early 2024 benefited from stronger engagement or higher-value use cases.
- Acquisition and product strategies must address falling per-user value, not just scale.

<br>

**3.2- Early LTV by Acquisition Channel** <br>
Which signup sources produce users who generate the most value in their first 180 days?

<p align="center">
  <img src="images/03_2_cohort_ltv_180d_per_acquisition_channel.png" width="85%">
</p>

#### Method
- Restrict users to **2024 signup cohorts**
- Calculate 180-day post-signup net revenue at the user level
- Aggregate cohort LTV by **acquisition channel and signup month**
- Compare early LTV performance across paid, organic, referral, and partner channels

#### Key Insights
- Employer partnership users consistently generate the highest 180-day LTV across cohorts.
- Referral users show strong early value generation, outperforming organic and paid channels.
- Organic users deliver moderate LTV but show clear decay in later cohorts.
- Paid acquisition users generate the weakest early LTV despite slower activation and higher acquisition costs.
- Channel-level LTV dispersion highlights a structural mismatch between **where users are acquired** and **where value is actually generated**.

#### **Business Implications**
- Employer partnerships and referrals deliver the strongest early LTV and should be prioritized.
- Paid acquisition produces the weakest value despite higher costs and slower activation.
- Channel-level LTV mismatch indicates inefficient capital allocation.
- Shifting acquisition mix toward high-LTV channels improves growth efficiency without increasing spend.

<br><br>

## 4 - Monetization Mechanics

**4.1- Overall Revenue Stack (GMV, Net Revenue, Take Rate)** <br>
How much transaction volume flows through the product, how much revenue AscentPAY captures, and how efficiently it monetizes that volume?

<p align="center">
  <img src="images/04_1_ revenue_stack_total.png" width="85%">
</p>

#### Method
- Restrict transactions to **monetizable spend activity** (card payments, bill pay, FX payments)
- Exclude top-ups and peer-to-peer transfers from GMV
- Aggregate monthly **GMV** and **net revenue** for calendar year 2024
- Compute take rate as `net revenue ÷ GMV`

#### Key Insights
- Net revenue grows steadily through the first half of the year, peaking mid-year before declining.
- Take rate remains **remarkably stable (~1.18%–1.30%)** across months.
- This indicates revenue changes are driven primarily by **transaction volume**, not pricing or fee expansion.
- Monetization efficiency is consistent, but revenue is highly sensitive to usage momentum.
- When activity slows, revenue falls proportionally, exposing limited pricing leverage.

#### **Business Implications**
- Stable take rate confirms pricing discipline but limits revenue upside without volume growth.
- Revenue sensitivity to transaction volume increases exposure to engagement slowdowns.
- Monetization efficiency is strong, but pricing leverage is limited.
- Growth initiatives must prioritize increasing transaction frequency and volume.

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
- Segment monetizable transactions by type (bill pay, card payments, withdrawals)
- Aggregate monthly net revenue by transaction channel
- Compare relative contribution and trend consistency across channels

#### Key Insights
- **Bill pay and card payments** are the dominant revenue drivers throughout the year.
- Withdrawals contribute meaningfully but remain a secondary revenue source.
- Revenue composition is relatively stable, with no single channel showing explosive growth.
- The lack of a breakout monetization channel limits upside without overall usage growth.
- The platform relies on **balanced transaction mix**, not a high-margin feature.

#### **Business Implications**
- Revenue is concentrated in bill pay and card payments, with no breakout monetization feature.
- A balanced mix provides stability but limits asymmetric upside.
- Lack of a high-margin channel constrains revenue expansion without usage growth.
- New monetization features could materially improve revenue resilience.

<br><br>

## 5 - Acquisition Efficiency

**5.1 - LTV vs CAC by Acquisition Channel** <br>
Do customers generate enough lifetime value within 180 days to cover their acquisition cost?

<p align="center">
  <img src="images/05_1_LTV_to_CAC_ratio.png" width="85%">
</p>

#### Method
- Calculate **180-day LTV** per user by acquisition channel
- Aggregate **customer acquisition cost (CAC)** by channel
- Compute **LTV-to-CAC ratio** as:  
  180-day LTV ÷ CAC
- Ratios above **100%** indicate channels that fully recover acquisition cost within 180 days

#### Key Insights
- **Referral users fully recover CAC (≈106%)**, making this the most efficient channel.
- **Employer partnerships perform well (≈74%)**, but do not fully pay back within 180 days.
- **Paid ads are highly inefficient (≈12%)**, failing to recover even a fraction of CAC.
- Organic acquisition delivers scale but lacks direct CAC attribution in this comparison.
- Overall, growth efficiency is **constrained by over-reliance on paid acquisition**.

#### **Business Implications**
- Referral acquisition is capital-efficient and self-sustaining.
- Employer partnerships are promising but require longer payback horizons.
- Paid acquisition destroys value at current performance levels.
- Scaling paid channels without structural improvement increases burn without growth.

<br>

**5.2 - CAC Payback Period by Acquisition Channel** <br>
How quickly does each acquisition channel generate enough revenue to repay its upfront acquisition cost?

<p align="center">
  <img src="images/05_2_CAC_payback_period.png" width="85%">
</p>

#### Method
- Track cumulative net revenue per user over time
- Measure **average days required to reach CAC breakeven**
- Calculate **percentage of users who repay CAC within 180 days**
- Report metrics by acquisition channel

#### Key Insights
- **Referral users repay CAC fastest (~78 days)** and at the highest completion rate (~31%).
- **Employer partner users repay more slowly (~86 days)** with moderate recovery rates (~24%).
- **Paid ads have extremely long payback (~121 days)** with almost no users recovering CAC (~3%).
- Many paid users **never repay CAC**, even after 180 days.
- This creates sustained capital drag and limits scalable growth.

#### **Business Implications**
- Fast payback channels enable reinvestment and compounding growth.
- Paid ads tie up capital for long periods with minimal recovery.
- Long payback windows increase risk during demand slowdowns.
- Payback speed should be a gating metric for acquisition scaling.

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

