# **2. Progressive Experimentation: Causal, DiD, Geo Tests & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

## 📘 Index

1. [Causal Inference](#causal-inference)  ❌  
   1.1. [Difference-in-Differences (DiD)](#11-difference-in-differences-did)  
   1.2. [Synthetic Control Method](#12-synthetic-control-method-)
   1.3. [Regression Discontinuity Design (RDD)](#13-regression-discontinuity-design-rdd)  
   1.4. [Instrumental Variables (IV)](#14-instrumental-variables-iv)  
   1.5. [Propensity Score Matching](#15-propensity-score-matching)  
   1.6. [Uplift Modeling](#16-uplift-modeling)  
   1.7. [Causal Diagrams & DAGs](#17-causal-diagrams--dags)  
   1.8. [Bayesian Causal Impact](#18-bayesian-causal-impact)
   1.9. [4-Cell RCT with holdout cells for incrementality testing](#19-4-cell-rct-with-holdout)

3. [Geo Experiments & Geo Lift Analysis](#geo-experiments--geo-lift-analysis)  ❌  
   2.1. Aggregate Geo-Based A/B Tests  
   2.2. Pre/Post Trends and Control Matching  
   2.3. Applications for Brand/Media Testing  

4. [Regression Models](#regression-models)  ❌  
   3.1. Simple Linear Regression  
   3.2. Multiple Linear Regression  
   3.3. Logistic Regression  

5. [Choosing & Designing the Right Causal Method](#choosing--designing-the-right-causal-method)  ❌  

6. [Design of Experiments (DoE)](#design-of-experiments-doe)  ❌  

7. [Libraries](#libraries) ❌  
   - `statsmodels` (OLS, logistic, fixed effects, DiD)
   - `econml` (CATE estimation, uplift modeling, IVs, meta learners)
   - `DoWhy` (causal graphs, identifiability, backdoor criteria)
   - `causalimpact` (Bayesian time series intervention model, ported from R to Python)
   - `PyMC`, `pymc3` (Bayesian modeling, priors, posteriors)
   - `scikit-learn` (base regression models, preprocessing)
   - `CausalML` (uplift models: S-learner, T-learner, X-learner)

8. Coding Packages ❌  

9. [Resources](#resources)  ❌  

   - [ ] PYMC-Marketing https://www.youtube.com/watch?v=RY-M0tvN77s  
   - [ ] Bayesian Marketing Science https://www.youtube.com/watch?v=5QgiixYjmTM&t=1320s
   - [ ] Diff-in-Diff Models https://www.youtube.com/watch?v=w56HI8YxLMQ&t=217s
   - [ ] Regression Discontinuity Design https://www.youtube.com/watch?v=TzdRl1OnQaw

---

## Brief Overview of Tests Under the Hood

| Method                        | What's Actually Tested                              | Under-the-Hood Test              |
|------------------------------|------------------------------------------------------|----------------------------------|
| **A/B Testing (RCT)**        | Mean difference between groups                      | **t-test** or **z-test**         |
| **Difference-in-Differences**| Pre-post changes across groups                      | **Regression + t-test**          |
| **Regression Analysis**      | Coefficient of treatment variable ≠ 0               | **t-test on β coefficient**      |
| **Propensity Score Matching**| Mean outcome difference post-matching               | **t-test** / **non-parametric**  |
| **Instrumental Variables**   | Effect of instrument on outcome (2SLS)              | **t-test** on 2SLS regression    |
| **CausalImpact**             | Post-treatment deviation from expected trend        | **Bayesian posterior test**      |
| **Uplift Modeling**          | Differential treatment effect per individual        | **Model-based; may test uplift > 0** |


## Causality
**Conditions to prove Causality:**

- Strong and statistically significant correlation
- Temporal precedence (cause must come before effect), shown in one of three ways:
   a. Clear chronological ordering (e.g., variable A occurs before B)
   b. Controlled experiments (e.g., random assignment of A, then measure B)
   c. Existence of a strong theoretical framework supporting the direction from A → B

> Note: Correlation alone is not sufficient for causality. You must rule out confounding factors and ensure the relationship isn’t spurious.

![440174565-23c8dfc8-67f0-4211-a088-f18c976a56cd](https://github.com/user-attachments/assets/b137e9f3-9351-47f8-8d51-8c5f6983f771)


## Causal Inference

### 1.1 Difference-in-Differences (DiD)
- Essentially a regression model.
- Measures causal effect in one metric among two groups
- Measures trend in each group pre and post treatment
- Then determines the difference between those two diff's: +ve or -ve result
- Critical to Have: Parallel Trends Assumption Pre-Treatment & Non-independent observations (important only if small sample size)
- Quasi-experimental Design: Uses non-equivalent control group.
- Usually Paired with techniques like propensity score matching to create a more reliable control group. (QUESTION: when to deem it necessary to apply such technique and not rely on the quasi-control group natural data?)
  
y=β 
0

 +β 
1
​
 D+β 
2
​
 T+β 
3
​
 (D×T)+u  

**Core Assumptions in Difference-in-Differences (DiD) & How to test for them**

1. **Linearity:** The relationship between the independent variables and the outcome is linear.
   - **Visual inspection**: Plot the relationship between predictors and outcome.
   - Consider adding polynomial terms or interaction terms if non-linear patterns are detected.

2. **Independence of Observations:** Each observation is independent of the others (no autocorrelation or spillover effects unless explicitly modeled).
   - For **time-series or panel data**, use:
     - Durbin-Watson test (autocorrelation)
     - Clustered standard errors to account for within-group correlation
   - Avoid overlapping treatments or spillovers between units.

3. **No Perfect Multicollinearity:** The independent variables are not perfectly correlated.
   - Check **Variance Inflation Factor (VIF)**: Rule of thumb: VIF > 5–10 → strong multicollinearity
   - Drop redundant variables or combine them.
     
4. **Zero Conditional Mean of Errors:** The error term \( u \) has an expected value of zero given the independent variables:  
   \(\mathbb{E}[u \mid D, T, D \times T] = 0\)
   - This is an assumption that **can't be directly tested** — it's a requirement of correct model specification.
   - Mitigate by:
     - Including relevant covariates
     - Avoiding omitted variable bias
     - Running robustness checks and placebo tests

5. **Homoscedasticity:** The variance of the error term is constant across all values of the independent variables.
   - Plot residuals vs. fitted values: Look for funnel shapes.
   - Use tests:
     - Breusch-Pagan test
     - White’s test

6. **Normality of Errors:** The error term is normally distributed — especially important for small samples to ensure valid confidence intervals and p-values.
   - Histogram or Q-Q plot of residuals
   - Shapiro-Wilk or Kolmogorov-Smirnov test (for small samples)
   - Note: Less critical with large samples due to Central Limit Theorem.

7. **Parallel Trends Assumption:** In the absence of treatment, the treated and control groups would have experienced the **same change over time** in the outcome.
   - Plot pre-treatment trends for treated vs. control groups
   - Run a **“placebo DiD”** using earlier pre-periods only
   - Add leads and lags of treatment variable in an **event study model** to test for pre-trends

---

### 1.2 Synthetic Control Method
_TODO: Add summary and applied notes._

### 1.3 Regression Discontinuity Design (RDD)

- **What It Is**  
  A quasi-experimental design that estimates the causal effect of a treatment assigned at a threshold or cutoff in a continuous forcing variable.

- **When to Use**  
  Use RDD when:
  - There’s a **continuous assignment variable** (forcing variable).
  - Treatment is applied only if the variable crosses a **cutoff**.
  - Units just above and below the cutoff are assumed to be similar (locally randomized).

- **Two Types of RDD:**
   1. **Sharp RDD:** Treatment assignment is fully determined by the cutoff in the forcing variable.
      - Example: Students get a scholarship only if their test score ≥ 85.
      - Interpretation: You’re estimating the jump in the outcome exactly at the cutoff.
      - Analysis: Local linear regression or polynomial regression on either side.

   2. **Fuzzy RDD:** Probability of receiving treatment increases sharply at the cutoff, but it's not deterministic.
      - Treatment assignment is not perfectly aligned with the cutoff. (e.g., some just below the threshold still get treated, or some above don't).
      - Example: A campaign is recommended for funding if score ≥ 85, but the decision is still subject to human review.
      - Interpretation: The cutoff serves as an **instrumental variable**.
      - Analysis: Estimate a local average treatment effect (LATE) using 2-stage least squares (2SLS).


- **Example (Paid Search Campaigns)**  
  - A new bidding strategy is triggered for campaigns with ROAS ≥ 2.0.
  - RDD compares outcomes (e.g. order value or GMV per customer) just above and just below this ROAS threshold.
  - The goal is to estimate the causal effect of that strategy near the threshold.

- **How to Estimate the Effect**  
  - Plot outcome vs. forcing variable around the cutoff.
  - Fit separate regression lines to both sides of the threshold.
  - The **jump** (discontinuity) at the cutoff estimates the treatment effect.
  - Use **local linear regression** and bandwidth tuning for precision.

- **Assumptions**  
  - **Continuity**: The relationship between the forcing variable and outcome is smooth in absence of treatment.
  - **No manipulation**: Subjects can’t precisely manipulate the forcing variable near the cutoff.
  - **Local Comparability**: Units near the threshold are comparable in observed and unobserved factors.

---

### 1.4 Instrumental Variables (IV)
_TODO: Add assumptions, 2SLS and examples._
One way to handle confounding variables and endogenous independent variables

### 1.5 Propensity Score Matching
_TODO: Add balancing, covariate matching logic._

### 1.6 Uplift Modeling
_TODO: Add T-Learner, X-Learner, meta-learners._

### 1.7 Causal Diagrams & DAGs
- Causal graphs help visualize causal assumptions and confounders.
- Used to determine valid adjustment sets via backdoor criteria.
- Tools: `DoWhy`, `dagitty`, `causalnex`

### 1.8 Bayesian Causal Impact
_TODO: Add causal impact implementation and use cases._

### 1.9 4 Cell RCT with Holdout

## Geo Experiments & Geo Lift Analysis

### 2.1 Aggregate Geo-Based A/B Tests
_TODO: Add methodology summary._

### 2.2 Pre/Post Trends and Control Matching
_TODO: Add design examples and metrics._

### 2.3 Applications for Brand/Media Testing
_TODO: Add use cases like YouTube lift or out-of-home campaigns._

## Regression Models

### 3.1 Simple Linear Regression
- Minimizes MSE.
- Assumes linearity, normality of errors, independence, homoscedasticity.

### 3.2 Multiple Linear Regression
- Adds assumption: no multicollinearity.
- Check with VIF and tolerance.
- Includes standardized vs unstandardized coefficients.
- R², adjusted R², standard error.
- Use dummy variables for categorical features (drop one as baseline).

### 3.3 Logistic Regression
- Binary classification via sigmoid function.
- Solved via maximum likelihood.
- Statistical significance tested using Wald’s z-test or chi-squared.

## Choosing & Designing the Right Causal Method !!!!!!!!!NEEDS CLEANUP!!!!!!

### Notes:
   - 


### Purpose:
Explain how to choose between DiD, Bayesian Causal Impact, Geo tests, or regression-based strategies for estimating treatment effects.

### Start with the Goal
- Estimate the **causal effect** of a treatment (e.g., campaign, feature) on an outcome (e.g., conversions, ROAS).
- Avoid bias from confounding, seasonality, or selection effects.

### Difference-in-Differences (DiD)
- **Use Case**: You have both treated and untreated groups over time.
- **Assumptions**:
  - Parallel trends between groups.
  - No spillovers or interference.
- **Strengths**: Simple design, good with panel data.
- **Weaknesses**: Sensitive to assumption violations, requires control group.

### Bayesian Causal Impact
- **Use Case**: One treated unit, time series with multiple pre-period predictors.
- **Mechanism**: Builds a pre-treatment model, forecasts counterfactual, compares actual to predicted.
- **Assumptions**: Stable pre-period relationship between outcome and predictors.
- **Strengths**: Uncertainty quantification, no need for control group.
- **Weaknesses**: Requires solid control variables; prior handling is critical.

### When to Use Which

| Situation                              | Use DiD                           | Use Bayesian Causal Impact           |
|----------------------------------------|-----------------------------------|--------------------------------------|
| Treated and control group available    | ✅ Yes                            | ❌ Not ideal                         |
| Only one treated unit (e.g., 1 geo)    | ❌ No                             | ✅ Yes                               |
| Long time-series pre-intervention      | ✅ Helpful                        | ✅ Essential                         |
| Need for probabilistic inference       | ❌ No                             | ✅ Yes                               |
| Simple, low-data setup                 | ✅ Simpler                        | ❌ Requires more modeling            |


| Situation                                           | Use A/B Test | Use DiD | Use Geo Test | Use RDD | Use Causal Impact |
|----------------------------------------------------|--------------|---------|--------------|--------|--------------------|
| Randomization is possible                          | ✅ Yes       | ❌ No   | ❌ No        | ❌ No | ❌ No              |
| You have pre/post data + treated & control groups  | ❌ No        | ✅ Yes | ✅ Yes       | ❌ No | ❌ No              |
| You have only 1 treated group (e.g. one region)    | ❌ No        | ❌ No  | ✅ Yes       | ❌ No | ✅ Yes             |
| Treatment assigned based on cutoff rule            | ❌ No        | ❌ No  | ❌ No        | ✅ Yes| ❌ No              |
| Need probabilistic uncertainty                     | ❌ No        | ❌ No  | ❌ No        | ❌ No | ✅ Yes             |
| Can’t randomize and have no clear control group    | ❌ No        | ❌ No  | ❌ No        | ❌ No | ✅ Yes             |


---

## Design of Experiments (DoE)

Design of Experiments (DoE) is a structured, statistical approach to **planning tests** that assess the effects of multiple factors (independent variables) on a measurable outcome (dependent variable).

### 🎯 Goals of DoE
   - Identify **which variables** significantly affect an outcome.
   - Understand **interactions** between variables.
   - Optimize performance with minimal testing effort.
   - Reduce cost and time compared to one-variable-at-a-time testing.

### 🧱 Common DoE Types

   - **Full Factorial Design**
     - Tests all possible combinations of factors and levels.
     - Best for small sets of variables.
     - Allows analysis of main effects and all interactions.
   
   - **Fractional Factorial Design**
     - Uses a **subset of combinations** to reduce test volume.
     - Assumes some higher-order interactions are negligible.
     - Efficient for testing 4+ variables.
   
   - **2-Level Factorial (2ⁿ)**
     - Each factor has 2 levels (e.g., low/high).
     - Ideal for screening key drivers.

### 📏 Related Concepts

- **Power Analysis & Sample Size Estimation**
  - Estimate how many observations per condition are needed.
  - Inputs: α (significance), power, MDE, number of groups.
  - Same fundamentals apply as in A/B testing.

- **Minimum Detectable Effect (MDE)**
  - Smallest effect size you'd care to detect.
  - Helps balance precision vs cost.

- **Blocking**
  - Account for known sources of variation (e.g., day of week).
  - Improves test precision by isolating uncontrollable noise.

### 🧠 When to Use
- Multivariate campaign testing (e.g., ad copy × bidding strategy)
- Budget allocation testing (portfolio × device × match type)
- Creative optimization across multiple attributes (headline × image × CTA)

---



