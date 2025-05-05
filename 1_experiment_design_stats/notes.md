# **1. Core Statistics & Experimentation Design**

## 📘 Index

1. [Statistical Testing](#statistical-testing)  ✅   
   1.1. [T-Tests](#t-tests)  
   1.2. [ANOVA](#anova)  
   1.3. [Chi-Square Tests](#chi-square-tests)  
   1.4. [Parametric vs Non-Parametric Alternatives](#parametric-vs-non-parametric-alternatives)  
   1.5. [Assumption Testing](#assumption-testing)  
   1.6. [Correlation](#correlation)

2. [Hypothesis Testing](#hypothesis-testing)  ✅   
   2.1. [Null vs. Alternative Hypotheses](#null-vs-alternative-hypotheses)  
   2.2. [Confidence Intervals & P-values](#confidence-intervals--p-values)  
   2.3. [Effect Sizes](#effect-sizes)  
   2.4. [Causality](#causality)

3. [Power Analysis & Sample Size Estimation](#power-analysis--sample-size-estimation)  ✅   
   3.1. [Minimum Detectable Effect (MDE)](#minimum-detectable-effect-mde)  
   3.2. [Sample Size Formula](#sample-size-formula)  
   3.3. [Trade-offs](#trade-offs)
   3.4. [Unequal Sample Split Testing](#Unequal-Sample-Split-Testing)

5. [A/B Testing Design](#ab-testing-design)  ✅   
   4.1. [Frequentist vs Bayesian A/B Testing](#frequentist-vs-bayesian-ab-testing)  
   4.2. [Sequential Testing and FDR Correction](#sequential-testing-and-fdr-correction)  
   4.3. [Confidence vs Credible Intervals](#confidence-vs-credible-intervals)  
   4.4. [Bayesian A/B Testing Concepts](#bayesian-ab-testing-concepts)

6. [Survival Analysis](#survival-analysis)  ✅   
   5.1. [Kaplan-Meier Curve](#kaplan-meier-curve)  
   5.2. [Log-Rank Test](#log-rank-test)  
   5.3. [Cox Regression](#cox-regression)

7. [Control Charts](#control-charts)  ✅
   
8. [Data Structure For Experiment Design & Analysis](#data-structure-for-experiment-design-and-analysis)  ✅   
   
9. [Libraries](#libraries)  ❌  
- `scipy.stats`
- `statsmodels.stats.api` (for t-tests, ANOVA, power analysis)
- `pingouin` (for effect sizes, CI)
- `bayespy`, `PyMC`, `pymc3` (for Bayesian A/B testing)
- `GeoLift` (R package; similar analysis can be replicated in Python)
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` (for exploratory & visual analysis)

10. Coding Packages  ❌  

11. [Resources](#resources)
- [ ] Data Tab: Full Lecture on Data Science Statistics https://www.youtube.com/watch?v=K9teElePNkk
- [ ] Statistical Power  https://www.youtube.com/watch?v=Rsc5znwR5FA&t=395s
- [ ] Power Analysis and Sample Size https://www.youtube.com/watch?v=VX_M3tIyiYk&t=246s

---

## Statistical Testing


### T-Tests

* One sample t-test: to see if a sample mean value is significantly different from the mean reference value  
* Independent Samples t-test: compare significant difference between the mean value of two independent samples (two drugs, campaigns, etc.)  
* Paired Samples t-test: compare means of two dependent groups (e.g., before and after treatment)

- t-test samples must be normally distributed (else use non-parametric t-test like Mann–Whitney U test which compares medians)  
- In an independent two-sample t-test, samples must be **equal variance (test with Levene’s test)**
- Null: no difference. Alt: significant difference.  
- Calculate t-statistic = (difference in means / standard error), then get the t-critical value for the sample’s degrees of freedom. If t-stat > t-critical → reject null
---
### ANOVA

* Extension of t-test when comparing more than two samples  
* **One-Way ANOVA**: is like an independent two sample t-test. one measurement across samples at one moment in time. It examines the effect of one independent categorical variable on a continuous variable.  
* **Two-Way ANOVA**: is like one way but tests the effect of two categorical independent variables on a continuous variable (effect on salary due to age and gender). it also evaluates the impact of the interaction of the two categorical variables.
* **Repeated Measures ANOVA**: it's like a paired t-test. Measure samples at three or more times times before and after a treatment and analyze the mean difference sample. Here samples are dependent (e.g. heart rate before workout, right after workour, 2hours after workout)
* **Mixed-Model ANOVA**: Combines repeated and between-subjects

- Requires normal distribution(if not, use Kruskal-Wallis-Test), equal variances (if not, use Welch-ANOVA), and no significant outliers. (plus for for repeated measures ANOVA, sphericity is required (Mauchly’s test)  
- F-statistic = between-group variance / within-group variance  
- If F > F-critical, reject null. Post-hoc tests are used to quantify the differences due to independent factors and interactions of multiple factors (effect size tests)
---
### Chi-Square Tests

* For nominal categorical variables, to see if there is a relationship between categorical variables (e.g. relationship between gender and favourite newspaper).
* Assumptions:
  - Expected frequencies per cell is greater than 5
  - account for different nominal categories without ordinal values or ranks (like categories of education (high school, Bsc, Msc, Phd). for rank copnsideration try spearman correlation, Mann-Whitney U-Test or Kruskal-Wallis-Test
* Null: no relationship; Alt: there is a relationship  
* Use chi-square statistic + degrees of freedom to determine p-value
---
### Parametric vs Non-Parametric Alternatives

- Parametric Tests are used when your sample data is normally distributed. if it's not, you should then use non-parametric tests.
- Parametric Tests run the analysis on the raw numerical data. Non-parametric tests usually rank the numerical values, use that to create normal distributions then run the analyses. Examples of parametric tests and their non-parametric test equivalents below:


| Test Type                          | Parametric Test                     | Nonparametric Test               | 
|-----------------------------------|-------------------------------------|----------------------------------|
| **One Sample**                    | Simple t-Test                       | Wilcoxon test for one sample     |
| **Two Dependent Samples**         | Paired Sample t-Test                | Wilcoxon Test                    |
| **Two Independent Samples**       | Unpaired Sample t-Test              | Mann–Whitney U Test              |
| **>2 Independent Samples**        | One-way (Factorial) ANOVA           | Kruskal–Wallis Test              |
| **>2 Dependent Samples**          | Repeated Measures ANOVA             | Friedman Test                    |
| **Correlation Between Variables** | Pearson Correlation                 | Spearman/Kendall's Tau     |
---

### Assumption Testing

**Normality Tests**  
1. Analytical Tests:
   - Kolmogorov-Smirnove Test (used to test other distribution types as well)
   - Shapiro-Wilk Test
   - Anderson-Darson (used to test other distribution types as well)

    Null Hypothesis: Data fits normal distribution, if p less than 0.05, reject null, non-normal distribution. p greater, fail to reject and assume normal distribution.

**Problems with analytical tests:** p-value depends on sample size. small samples mostly yield non-representative large values. Therefore graphical tests are more frequently used.

3. Graphical Test:
    - Normal histogram plotting to visually detect a bell curve
    - Quantile-Quantie Plot: Normally distributed data points wold follow the disagonal line plotted as reference. non-normal would typical form an S-shape instead
      
**Variance Equality**  
- Levene’s Test  
- Null: equal variance. If p < 0.05 → reject → use **Welch's t-test** instead of a t-test which requires homogenity of variance.
---

### Correlation
Goal: Determine strength and direction of correlation (usually a value between -1 to 1)

**Pearson Correlation Coefficient (r)**
* Null: no corr, alt:corr
* r tells us the corr, running a t-test tells us if r is significantly different from zero.
* **Assumptions:**
  - Only works on metric variables
  - only detects linear relationships, non-linear relationships won't be detected
  - If we're using r to test a hypothesis (We'd need to run t-test to prove statistical significance, therefore the two variables must be normally distributed).

**Spearman Correlation Coefficient (rs)**
* non-parametric equivalent of pearson correlation coeff (assign ranks rather than raw numbers).
* Spearman is equal to pearson when done on ranks.

**Kendall's tau**
* Non-parametric equivalent of pearson correlation and variables need to only have ordinal scale levels (numerical or ordinal but not categorical nominal).
* Exactly the same as spearman but should be preferred over spearman if very few data with many rank ties available.

**Point-Biserial Correlation Coefficient (rpb)**
* A special case of pearson correlation. Examines relationship between dichotomous variable and a metric variable.
* Dichtomous variable is a nominal one with two values (gender M/F, smoking Y/N, etc.), metric variable is like age, weight or salary.
* Provides same p-value as an independent t-test.
* To test statistical significance of this correlation, metric variable must be normally distributed, otherwise t-value and p-value can't be reliably interpreted.
---

## Hypothesis Testing

### Null vs. Alternative Hypotheses

- A **hypothesis test** evaluates evidence from a sample to make inferences about a population.
- **Null hypothesis (H₀)**: Assumes no effect or no difference. It's the default assumption.
- **Alternative hypothesis (H₁ or Hₐ)**: Suggests there is an effect or difference.
- Example:  
  - H₀: There is no difference between campaign A and B  
  - H₁: There is a statistically significant difference between campaign A and B

We reject or fail to reject the null based on the p-value and our chosen significance threshold (e.g., α = 0.05).


### Confidence Intervals & P-values


- A **p-value** measures how likely it is to observe the data (or something more extreme) **assuming the null hypothesis is true**.
  - A small p-value (typically < 0.05) means the observed result is unlikely under H₀, and we **reject** H₀.
  - A large p-value suggests there is **insufficient evidence** to reject H₀.

- A **confidence interval (CI)** provides a range of plausible values for a population parameter (like a mean or proportion).
  - A **95% CI** means: if we repeatedly sampled and calculated a CI, 95% of those intervals would contain the true population value.
  - CI gives both the **effect size** and its **precision**.

### Effect Sizes

- **Effect size** measures the **magnitude** of an observed effect, independent of sample size. Depending on the test you're running, the effect could be the strength of a difference or correlation.
- Helps quantify **practical significance**, not just statistical significance.
- Common effect size metrics:
  - **Cohen’s d**: For mean differences in t-tests (0.2 = small, 0.5 = medium, 0.8 = large)
  - **r²**: Proportion of variance explained by model (for regression)
  - **η² (eta squared)**: Effect size in ANOVA contexts



### Causality

**Conditions to prove Causality:**
1. **Strong and statistically significant correlation**
2. **Temporal precedence** (cause must come before effect), shown in one of three ways:
   a. Clear **chronological ordering** (e.g., variable A occurs before B)  
   b. **Controlled experiments** (e.g., random assignment of A, then measure B)  
   c. Existence of a **strong theoretical framework** supporting the direction from A → B

> Note: Correlation alone is **not sufficient** for causality. You must rule out **confounding factors** and ensure the relationship isn’t spurious.

![Distinguishing-third-variables-mediators-moderators-confounders-and-colliders](https://github.com/user-attachments/assets/23c8dfc8-67f0-4211-a088-f18c976a56cd)


---

## Power Analysis & Sample Size Estimation for A/B Testing

Goal: Estimate how much data you need to detect a meaningful effect with confidence.

Power = 1 − 𝛽

1−β: Probability of detecting a real effect (usually set to 0.8 = 80%) **i.e. The probability of correctly rejecting the null.**
α (Type I error): Risk of a false positive (commonly 0.05)
β (Type II error): Risk of a false negative (commonly 0.2)
→ Power is directly tied to Type II error

### Minimum Detectable Effect (MDE)
    This is the minimum effect we want to be able to detect in our experiment (e.g. 2% absolute increase in the conversion rate).

### Sample Size Formula

\[ n = \frac{2 \cdot (Z_{1-\alpha/2} + Z_{1-\beta})^2 \cdot \bar{p}(1 - \bar{p})}{(p_1 - p_2)^2} \]

- Resulting n is the required sample size per group (not total)
- Multiply by 2 for total sample size for both control and variant (If A/B test, or more if 3 groups for example)

### Trade-offs

| Factor | Effect |
|--------|--------|
| Lower α | Fewer false positives, more data |
| Lower β (higher power) | Fewer missed effects, more data |
| Smaller MDE | More data needed |


### Inputs for Sample Size Calculation
- Baseline rate (e.g. 10% conversion)
- MDE (e.g. +2% absolute = 12%)
- α = 0.05 (significance level)
- Power = 0.8

🔁 Error Balance & Trade-Offs
| Lower α (Type I error) | ➖ Fewer false positives<br>➕ Need more data |
| Lower β (higher power) | ➖ Fewer false negatives<br>➕ Need more data |
| Smaller MDE | ➕ Detect subtle effects<br>➖ Much larger sample required |

**Ensures test is neither underpowered (miss real effects) nor wasteful**


### Unequal Sample Split Testing

### 🔄 Unequal Split Testing
- Allocate traffic unevenly (e.g., 90% A, 10% B) to reduce risk.
- Requires **larger total sample size** to detect same effect.
- **Adjusted formula:**  

n = equal_sample_size × ((1 + k) / (4k)), where k = n_A / n_B

- Works with Welch’s t-test for continuous variables or Z-test for proportions, binary outcomes like conversions.

---

## A/B Testing Design

### Frequentist vs Bayesian A/B Testing

   #### Frequentist A/B Testing
   - Relies on **fixed sample size** and **p-values**.
   - Null hypothesis (H₀): no difference between A and B.
   - Reject H₀ if p-value < α (e.g. 0.05).
   - **Not safe to peek** at results mid-test (peeking inflates Type I error).
   - Requires pre-calculated sample size via power analysis.
   - Final decision is binary: _statistically significant_ or not.
   
   #### Bayesian A/B Testing
   - Based on **Bayes’ Theorem**:
      Posterior ∝ Prior × Likelihood
   - Outputs **probability distributions** instead of p-values.
   - Answers intuitive questions like:
   - “What is the probability B is better than A?”
   - Allows **continuous monitoring** — no penalty for peeking.
   - Uses **credible intervals** instead of confidence intervals.
   - Works well with smaller samples or prior information.
   
   #### ⏱ Bayesian Early Stopping
   - Continuously update posterior as new data arrives.
   - Common stopping rules:
   - Stop if `P(B > A) > 0.95` → B is better
   - Stop if `P(B > A) < 0.05` → B is worse
   - Optional: use **expected loss** or **regret minimization** to guide decisions.
   - Safer and more flexible than frequentist stopping; avoids p-hacking.
   - Avoids p-value hacking; allows for real-time decision making.
   - Use expected loss or credible intervals as stopping rules.
   
   #### When to Use Bayesian
   - You want **probabilistic interpretation**
   - Traffic is low or experiments are costly
   - You want to incorporate **prior knowledge**
   - You may need **early decisions**


### Sequential Testing and FDR Correction

**Sequential A/B Testing:**
- Frequentist method to **safely monitor results during a test**.
- Uses **adjusted thresholds** (e.g., O'Brien-Fleming bounds).
- Can stop early without inflating Type I error.
- Common designs:
   - Group Sequential Testing
   - Sequential Probability Ratio Test (SPRT)

**FDR Correction (False Discovery Rate) (For multiple experiments, samples and tested metrics)**
- Used when testing **multiple hypotheses** (e.g., multiple metrics or variants).
- Controls **expected proportion of false positives** among discoveries.
- **Benjamini-Hochberg procedure**:
   1. Sort p-values in ascending order: `p₁, p₂, ..., pₘ`
   2. Compare each `pᵢ` to:
      ```
      (i / m) × Q
      ```
      where `i` = rank, `m` = total tests, `Q` = FDR level (e.g. 0.05)
   3. Largest `pᵢ` passing the threshold → all p-values before it are significant.
   - Less conservative and more powerful than Bonferroni correction.

### Confidence vs Credible Intervals

- **Frequentist confidence interval**: Based on repeated sampling; says nothing about probability of parameters.
- **Bayesian credible interval**: Directly represents the **probability** that the parameter lies within the interval, given the data and prior beliefs.

### Bayesian A/B Testing Concepts

   **Why It Matters:**
   - Gives probability-based conclusions (e.g. "B is better than A with 95% certainty")
   - Allows continuous monitoring without p-value hacking.
   - Useful with small samples or historical priors.
   
   **When to Use**
   - Small samples or low-traffic tests
   - Want interpretable probability statements
   - Plan to monitor results continuously
   - Prior experiments inform current ones
     
   **What to Know**

   #### 🔹 Bayesian Basics

   - **Prior**: Represents your belief about a parameter before seeing the data.  
     Example: Based on past campaigns, we believe CVR is around 5%.
   
   - **Likelihood**: The probability of observing the current data given different parameter values.  
     This comes from your actual experiment.
   
   - **Posterior**: Updated belief after seeing the data.  
     Calculated using Bayes’ Theorem:
   
     \[
     \text{Posterior} \propto \text{Prior} \times \text{Likelihood}
     \]
   
   - **Credible Interval**: The Bayesian version of a confidence interval.  
     A 95% credible interval means there's a 95% probability the true value lies within that range.
   
   - **Bayesian vs Frequentist**:  
     - Bayesian interprets probability as **degree of belief** (based on both prior + data).  
     - Frequentist sees probability as **long-run frequency** of events in repeated experiments.

---

   #### 🔹 Bayesian A/B Testing
   
   - Used to compare two variants (A and B) using probability rather than p-values.
   
   - For binomial outcomes (e.g. conversions), we use the **Beta distribution**:
     - If A has `a_successes` and `a_failures`, its posterior is:  
       \[
       \text{Beta}(a_{\text{prior}} + a_{\text{successes}}, b_{\text{prior}} + a_{\text{failures}})
       \]
   
   - For each variant, simulate thousands of samples from their posteriors and compare (possibly using Monte-Carlo Simulation):
     - Calculate \[
     P(\text{B} > \text{A})
     \]
     — the probability that B is better than A.
   
   - You can also compute:
     - **Expected uplift**
     - **Expected loss** of choosing one over the other

---

   #### 🔹 Applications
   
   - **CVR / CTR Testing**:  
     Estimate conversion rate distributions and choose the version with highest probability of being best.
   
   - **Revenue & Lift Measurement**:  
     Extend Bayesian testing to model not just conversion rates, but also **average order value** or **incremental ROAS**.
   
   - **Geo Experiments**:  
     Incorporate prior campaign lift data across geos or use **hierarchical priors** when multiple markets share structure.

---

   #### 🔹 Priors
   
   - **Flat / Uninformative Priors**:  
     Use when you have no prior knowledge (e.g., `Beta(1,1)` = uniform).
   
   - **Informative Priors**:  
     Use when past data or domain expertise is available.  
     Example: "Based on past performance, we expect CVR ~ Beta(20, 380)" (i.e. 5%).
   
   - Good priors help regularize results when sample sizes are small or noisy.

---

   #### 🔹 Decision Rules
   
   - Make decisions using **posterior probabilities** instead of binary p-values:
     - E.g., choose B if  
       \[
       P(B > A) > 0.95
       \]
   
   - Or use **expected loss minimization**:
     - Simulate losses from choosing the worse variant
     - Pick the one with the **lower expected cost** of being wrong

---

   ✅ Summary:
   Bayesian testing gives richer, more intuitive results like:
   - "There is a 97.5% chance variant B is better than A"
   - "The expected uplift from switching to B is 1.2%, with 95% credible interval of [0.4%, 2.3%]"
   
   Perfect for business decision-making under uncertainty.

---

## Survival Analysis

Statistical analyses concerned with analyzing how much time runs out until a certain event takes place.
- Example: analyzing how a person dies after being diagnosed by a disease, or time to retunr to work afterburnout leave.

Goals of survival analysis:

1. Estimate time until an event occurs (e.g. churn, failure, death) (what is robability of event X at time t)
2. Handle censored data (subjects that haven’t experienced the event yet)
3. Compare time-to-event across groups (e.g. treatment vs. control)
4. Model the effect of variables on event timing (via hazard rates)
5. Calculate survival probabilities over time
6. Identify risk factors influencing event likelihood (Cox regression)

   
### Kaplan-Meier Curve

- time on x-axis
- survival rate on y-axis (1 at top, 0 at bottom)
- Example at t 5years, survival rate is 0.7. which means at t5, there's a 70% chance events hasn't occured yet.
- Kaplan Meier Curves Do censoring for data (very unique): Where it partially accounts for events that happen before or after the observation time period, unlike a regression model which would just ignore the data point.

**Two tests for testing effect on KM curves**
- Log rank to see if there's a diff in KM curve when changing a variable across two samples. Cox Regression if you're also testing for influence of more variables

#### 🔍 Key Differences Between Log-Rank Test and Cox Regression

| Feature                     | Log-Rank Test                                                   | Cox Proportional Hazards Regression                                   |
|----------------------------|------------------------------------------------------------------|------------------------------------------------------------------------|
| **Goal**                   | Test if two or more survival curves are significantly different | Estimate the effect of covariates (e.g. age, channel) on survival time |
| **Type of test**           | Non-parametric (no shape assumptions)                           | Semi-parametric (assumes proportional hazards)                         |
| **Input**                  | Group/category (e.g. Group A vs. Group B)                       | Continuous or categorical predictors                                  |
| **Output**                 | p-value (tests difference between groups)                       | Hazard ratios + coefficients for each variable                         |
| **Adjust for covariates?**| ❌ No                                                             | ✅ Yes                                                                 |
| **Effect size?**           | ❌ No — only detects difference presence                         | ✅ Yes — quantifies variable impact on hazard                          |
| **Assumes proportional hazards?** | ✅ Yes                                                   | ✅ Yes                                                                 |
| **Visual companion**       | Kaplan-Meier curves                                              | Survival curves by covariate                                          |



🧠 Summary in Plain Terms:
🧪 Log-Rank Test:
- Used when comparing two or more survival curves
- Answers: "Are the survival experiences in these groups statistically different?"
- No control for other variables

📈 Cox Regression:
- Used when modeling how multiple variables affect survival
- Answers: "How does each variable (e.g. age, ad channel, platform) impact the risk of event over time?"
- Adjusts for multiple covariates and gives hazard ratios (interpretable effect sizes)

✅ When to Use:
Use Log-Rank Test for:

- A/B test-style comparisons
- Simple group comparisons (e.g., churn rate by user group)

Use Cox Regression for:

- Real-world modeling with multiple influencing factors
- Need for interpretation (how much faster/slower people churn, die, convert, etc.)


---

## Control Charts

**📊 Key Points**
Purpose: Monitor process stability over time
Used for: Detecting unusual variation (signal vs. noise)
Tracks: Metric over time (e.g. conversion rate, ROAS, defects)

**📐 Components**
- Center Line (CL): Process average
- UCL / LCL: Control limits = mean ± 3 standard deviations
- X-axis: Time or sequence
- Y-axis: Metric value

**✅ In-Control Process**
- Points vary randomly within limits
- No clear trends or patterns

**❌ Out-of-Control Signals**
- Point outside UCL/LCL
- Sudden shifts or trends
- Repeated points near limits

**🧪 Common Use Cases**
- Marketing: Monitor ROAS, CTR, bounce rate
- Product: Funnel drop-off, error rates
- Manufacturing: Defect tracking
- Support: Call durations, wait times

---

## Data Structure For Experiment Design and Analysis

#### 📏 Data Breakdown for Sample Size Calculation

- Define:
  - **Primary KPI** (e.g., CVR, ROAS, CPC)
  - **Baseline value** (e.g., 5% conversion rate)
  - **Minimum Detectable Effect (MDE)** (e.g., +1% absolute uplift)
  - **Significance level (α)** (typically 0.05)
  - **Power (1 - β)** (typically 0.8)
- Use formulas or tools to compute **sample size per variant**
- Important: account for **traffic allocation** if using unequal splits (e.g., 90/10 A/B)

---

#### Data Structure for Running Tests

- **User-level data** (recommended):
  - Each row = one click/session with:
    - `user_id`, `campaign_id`, `variant`, `click_date`
    - outcome variables (converted: 0/1, revenue: €X, spend: €Y)
  - Enables flexible modeling (t-tests, regression, logistic)

- **Time-series data** (for budget/pacing & trends):
  - Daily or hourly aggregation:
    - `date`, `campaign_id`, `variant`, `impressions`, `clicks`, `conversions`, `spend`, `revenue`
  - Useful for:
    - Geo experiments
    - Pre-post analysis
    - Control matching
    - Interrupted time-series models

- **Aggregated campaign-level data** (simplified):
  - Use for reporting & simple z-tests:
    - Totals per group: impressions, clicks, conversions
    - Compute CVR, CTR, CPC, ROAS manually

---

#### 🔍 Paid Search-Specific Metrics to Track

- Click-level:
  - `search_query`, `ad_copy_id`, `keyword_match_type`, `device`, `geo`
  - `cost`, `cpc`, `quality_score`, `ad_position`, `impression_share`

- Conversion-level:
  - `conversion_value`, `conversion_category`, `time_to_convert`

- Derived metrics:
  - CVR = conversions / clicks
  - ROAS = revenue / spend
  - AOV = revenue / conversions
  - CPA = spend / conversions

---

#### 🧠 Best Practices

- ✅ Include `variant` or `experiment_group` assignment explicitly
- ✅ Randomize users/campaigns *before* the experiment starts
- ✅ Keep consistent attribution windows (e.g., 7-day post-click)
- ✅ Avoid filtering mid-test (e.g., removing mobile traffic after launch)
- ✅ Store both **raw and aggregated** data for flexibility
- ❌ Don't rely solely on platform UI exports (can be lossy or rounded)

---

#### 📦 Ideal Columns for Paid Search A/B Dataset

| Column              | Type        | Description                            |
|---------------------|-------------|----------------------------------------|
| `user_id`           | string/int  | Unique identifier                      |
| `campaign_id`       | string      | Search campaign name or ID             |
| `variant`           | string      | A / B / test group                     |
| `click_date`        | date        | Timestamp of click                     |
| `converted`         | binary      | 0 or 1 (conversion occurred)           |
| `conversion_value`  | float       | Revenue if converted                   |
| `spend`             | float       | Cost of click                          |
| `device_type`       | category    | Mobile / Desktop / Tablet              |
| `keyword_match`     | category    | Exact / Phrase / Broad                 |

---

### 📈 Measuring ROAS Across Multiple Portfolios & Campaign Strategies

---

#### 💡 What is ROAS?

\[
\text{ROAS} = \frac{\text{Revenue}}{\text{Ad Spend}}
\]

- Higher = more efficient ad spend.
- Can be measured:
  - Per **campaign**, **ad group**, or **keyword**
  - Across **time**, **geo**, or **portfolio**

---

#### 🧠 Why It Gets Tricky

- **Portfolios** may contain different campaign types (brand vs generic, mobile vs desktop).
- **Spend distribution** is not equal (e.g. 80/20 budget split).
- ROAS can be influenced by:
  - Audience targeting
  - Seasonality
  - Bid strategies (manual vs tCPA vs max ROAS)
  - Device/geolocation breakdown

---

#### 📊 Best Practices for Multi-Campaign ROAS Measurement

- ✅ **Normalize** campaign performance:
  - Use weighted averages:
    \[
    \text{Weighted ROAS} = \frac{\sum_i (\text{Revenue}_i)}{\sum_i (\text{Spend}_i)}
    \]
  - Don't average ROAS ratios across campaigns (it’s misleading).

- ✅ **Segment ROAS by strategy**:
  - Manual vs automated bidding
  - Broad vs exact match keywords
  - Geo, device, or audience segments

- ✅ **Use regression to adjust for confounders**:
  - Model:  
    \[
    \text{ROAS} = \beta_0 + \beta_1 \cdot \text{Strategy Type} + \beta_2 \cdot \text{Device} + \dots
    \]
  - Helps isolate effect of portfolio/bidding strategy on ROAS.

- ✅ **Pre/Post or Matched Control Analysis**:
  - For strategy changes (e.g. switching from tCPA to MaxROAS), compare:
    - Pre vs post periods
    - Treatment vs similar control campaigns

---

#### 📦 Suggested Data Structure

| Column           | Type      | Description                             |
|------------------|-----------|-----------------------------------------|
| `campaign_id`    | string    | Unique campaign or portfolio ID         |
| `strategy_type`  | string    | Manual, tCPA, MaxROAS, etc.             |
| `date`           | date      | Day-level granularity                   |
| `spend`          | float     | Ad spend in EUR                         |
| `revenue`        | float     | Tracked revenue                         |
| `device`         | category  | Device type                             |
| `geo`            | category  | Location/country                        |

---

#### 🧪 Recommended Metrics

- ROAS
- CPA
- CVR
- Average Order Value (AOV)
- Impression Share
- Click Share
- Budget utilization

---
