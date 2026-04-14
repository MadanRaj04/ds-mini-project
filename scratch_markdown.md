# Hypothesis Testing — Churn Prediction

In this notebook we test **15 hypotheses** about what makes a customer churn.
Each hypothesis follows the same simple pattern:

1. State what we think is happening (the hypothesis)
2. Pick the right statistical test for the type of data
3. Run the test
4. Read the result and say what it means in plain English

**What is a p-value?**  
A p-value tells us the probability that we would see this result just by chance.  
- p < 0.05 → the result is statistically significant (very unlikely to be random)
- p ≥ 0.05 → we cannot confidently reject the null hypothesis

**Tests used:**
- **Chi-Square test** — checks if two categorical things (e.g. band vs churn) are related
- **T-test** — checks if the average of something (e.g. tenure years) differs between two groups
- **Mann-Whitney U test** — like a t-test but works even when data is not normally distributed
- **Point-Biserial Correlation** — measures how strongly a numeric feature is linearly related to churn
---
## H1 — Customers who expressed desire to cancel churn more

**Hypothesis:** Customers who said they wanted to cancel on a renewal call will churn at a higher rate than those who did not.  
**Test:** Chi-Square — desire_to_cancel_clean and churn variables are categorical 

**Null hypothesis:** There is no relationship between expressing desire to cancel and actually churning.
---
## H2 — Newer customers churn more than long-term customers

**Hypothesis:** Customers in their first year have not built enough loyalty yet, so they leave at a higher rate.  
**Test:** T-test — compare average tenure years between churned and retained groups.  
**Null hypothesis:** There is no difference in average tenure between churned and retained customers.
---
## H3 — Customers with Status Score = 0 churn at a much higher rate

**Hypothesis:** A status score of 0 means the customer has no active accreditation, so the membership feels worthless to them — they are much more likely to leave.  
**Test:** Chi-Square — status_score (0 vs non-zero) vs churn (0/1).  
**Null hypothesis:** Status score = 0 has no effect on churn.
---
## H4 — Customers who mentioned financial hardship are more likely to churn

**Hypothesis:** Customers who mentioned financial difficulty in email interactions cannot afford the renewal and will leave.  
**Test:** Chi-Square — financial_hardship_mentioned (Yes/No) vs churn.  
**Null hypothesis:** Mentioning financial hardship has no relationship with churn.
---
## H5 — Customers who requested a discount are more likely to churn

**Hypothesis:** Asking for a discount signals price sensitivity. Customers who ask for a discount but do not get one (or feel the price is still too high) are more likely to leave.  
**Test:** Chi-Square — discount_requested_flag (1/0) vs churn.  
**Null hypothesis:** Requesting a discount has no relationship with churn.
---
## H6 — Customers with a dissatisfied CC sentiment are more likely to churn

**Hypothesis:** Customers who are marked as Dissatisfied during a customer care call have an unresolved issue. They are more likely to leave at renewal.  
**Test:** Chi-Square — cc_contractor_sentiment (Dissatisfied vs Satisfied/Neutral) vs churn.  
**Null hypothesis:** CC call sentiment has no relationship with churn.
---
## H7 — Customers who raised a serious complaint are more likely to churn

**Hypothesis:** A serious complaint indicates deep dissatisfaction. Even if the complaint is resolved, the bad experience may push the customer to leave at renewal.  
**Test:** Chi-Square — serious_complaint_flag (1/0) vs churn.  
**Null hypothesis:** Raising a serious complaint has no effect on churn.
---
## H8 — Customers the agent had to chase more often are more likely to churn

**Hypothesis:** If the agent had to chase a customer multiple times via email, it means the customer is not engaging. Low engagement at renewal time = higher churn risk.  
**Test:** Chi-Square — agent chase level (Low/Medium/High) vs churn.  
**Null hypothesis:** How often the agent had to chase the customer has no effect on churn.
---
## H9 — Customers dissatisfied with renewal price in emails are more likely to churn

**Hypothesis:** When a customer explicitly says they are unhappy with the renewal price in an email, price is the main driver of their potential churn.  
**Test:** Chi-Square — crm_dissatisified_with_renewal_price (Yes/No) vs churn.  
**Null hypothesis:** Email-expressed price dissatisfaction has no effect on churn.
# H10 — Customers with negative sentiment churn more
Hypothesis: Customers categorised as having negative sentiment during their renewal call churn at a higher rate.<br>
Test: Chi-Square — sentiment_category vs churn<br>
Null hypothesis: There is no association between sentiment category and churn.
# H11 — Membership band influences churn rate
Hypothesis: Customers on lower membership bands churn at a higher rate than those on higher bands.<br>
Test: Chi-Square<br>
Null hypothesis: There is no association between membership band and churn rate.<br>
