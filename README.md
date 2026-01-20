# WIP ( Jan 19 2026 )

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
  
<br><br>

## 3 - Customer Value (LTV)**

**3.1- How does 180-day LTV vary by signup cohort?**

<p align="center">
  <img src="images/03_1_cohort_ltv_180d.png" width="85%">
</p>

<br>

**3.2- Which acquisition channels generate the strongest early LTV?**

<p align="center">
  <img src="images/03_2_cohort_ltv_180d_per_acquisition_channel.png" width="85%">
</p>

<br><br>

## 4 - Monetization Mechanics**

**4.1- What is the overall revenue stack (GMV, net revenue, take rate)?**

<p align="center">
  <img src="images/04_1_ revenue_stack_total.png" width="85%">
</p>

<br>

**4.2- How does the revenue stack differ by acquisition channel?**

<p align="center">
  <img src="images/04_2b_ revenue_stack_per_channel_1.png" width="85%">
</p>

<p align="center">
  <img src="images/04_2b_ revenue_stack_per_channel_2.png" width="85%">
</p>

<br><br>

## 5 - Acquisition Efficiency

**5.1 - Does LTV justify CAC by acquisition channel?**

<p align="center">
  <img src="images/05_1_LTV_to_CAC_ratio.png" width="85%">
</p>

<br>

**5.2 - How long does it take to recover CAC (payback period)?**

<p align="center">
  <img src="images/05_2_CAC_payback_period.png" width="85%">
</p>

<br><br>

## 6 - Revenue Concentration & Risk

**6.1 - Are results skewed by extreme users (IQR-based revenue outliers)?**

<p align="center">
  <img src="images/06_1_IQR_revenue_outliers.png" width="85%">
</p>

<br>

**6.2 - How concentrated is revenue across users (Pareto curve analysis)?**

<p align="center">
  <img src="images/06_2_pareto_ltv_180d.png" width="85%">
</p>











