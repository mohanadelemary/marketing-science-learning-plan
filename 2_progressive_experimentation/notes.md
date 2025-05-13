# **2. Progressive Experimentation: Causal, DiD, Geo Tests & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

## 📘 Index

1. [Causal Inference](#1-causal-inference)  ✅  
   1.1. [Causal Diagrams & DAGs](#11-causal-diagrams--dags)  
   1.2. [Handling Confounders in Regression on Observational Data](#12-handling-confounders-in-regression-on-observational-data)  

   **Quasi-Experimental Methods**  
   1.3. [Difference-in-Differences (DiD)](#13-difference-in-differences-did)  
   1.4. [Synthetic Control Method](#14-synthetic-control-method)  
   1.5. [Regression Discontinuity Design (RDD)](#15-regression-discontinuity-design-rdd)  
   1.6. [Instrumental Variables (IV)](#16-instrumental-variables-iv)  
   1.7. [Propensity Score Matching (PSM)](#17-propensity-score-matching-psm)   

   **Causal Machine Learning**  
   1.8. [Bayesian Causal Impact](#18-bayesian-causal-impact)  
   1.9. [Uplift Modeling](#19-uplift-modeling)  

   **Other Experiment Design**  
   1.10. [4-Cell RCT with Holdout Cells for Incrementality Testing](#110-4-cell-rct-with-holdout-cells-for-incrementality-testing)  

2. [Regression Models](#2-regression-models)  ✅  
   2.1. Simple Linear Regression  
   2.2. Multiple Linear Regression  
   2.3. Logistic Regression  

3. [Choosing & Designing the Right Causal Method](#3-choosing--designing-the-right-causal-method)  ✅  

4. [Example Analyses for Paid Search & How to Do Them](#4-example-analyses-for-paid-search--how-to-do-them)  ✅  

5. [Design of Experiments (DoE)](#5-design-of-experiments-doe)  ✅  

6. [Libraries](#6-libraries)  ✅  

7. Coding Packages ❌  

8. [Resources](#resources)  ❌  

   - [ ] PYMC-Marketing https://www.youtube.com/watch?v=RY-M0tvN77s  
   - [ ] Bayesian Marketing Science https://www.youtube.com/watch?v=5QgiixYjmTM&t=1320s
   - [ ] Diff-in-Diff Models https://www.youtube.com/watch?v=w56HI8YxLMQ&t=217s
   - [ ] Regression Discontinuity Design https://www.youtube.com/watch?v=TzdRl1OnQaw
   - [ ] Causal Impact with Google https://www.youtube.com/watch?v=GTgZfCltMm8&list=PLrEu3Zdeqm1MORDsMxDkIG-8UQobZzXmp
   - [ ] Insrumental Variable Method for Endogeneity https://www.youtube.com/watch?v=GJp4uU_3kjY

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

---

## 1. Causal Inference

### 1.1 Causal Diagrams & DAGs

- Causal graphs help visualize causal assumptions and confounders.
- Used to determine valid adjustment sets via backdoor criteria.
- **Tools: `DoWhy`, `dagitty`, `causalnex`**
- **DAG (Directed Acyclic Graph)**: A visual representation of causal relationships between variables  
- **Nodes**: Variables (e.g., X, Y, Z)  
- **Edges**: Arrows showing causal direction (e.g., X → Y)

**- Why Use DAGs** 
- Identify **confounders**, **mediators**, and **colliders**
- Guide decisions on which variables to control for
- Detect **bias sources** in causal inference

**- Key Terms**
- **Causal Path**: Sequence of arrows from cause to effect  
- **Backdoor Path**: A non-causal path from X to Y that introduces confounding  
- **Collider**: A variable influenced by two paths (X → Z ← Y) — **do not control**  
- **Confounder**: Common cause of X and Y (Z → X, Z → Y) — **control for these**

**- Adjustment Rules**
- Use the **Backdoor Criterion**: Block all backdoor paths from X to Y  
- **Do not adjust for:**
  - **Colliders**
  - **Mediators** (if estimating total effect)

**- Example DAGs**

   1. **Confounding Example**  
      Z → X → Y
      Z → Y
      
      - Z is a **confounder**  
      - Adjust for Z to estimate X → Y

   2. **Collider Example**  
      X → Z ← Y
      
      - Z is a **collider**  
      - Adjusting for Z opens a spurious path — causes bias

   3. **Mediation Example**  

      X → M → Y

      - M is a **mediator**
      - Don’t control for M if estimating total effect of X on Y

**- Best Practices**

   - Use DAGs **before analyzing data**
   - Only control for variables that block **backdoor paths**  
   - Use tools like:
   - [`dagitty.net`](https://www.dagitty.net/)
   - Python/R packages for DAGs and causal analysis

**- Limitations**
   - DAGs require **domain knowledge** to draw correctly  
   - Cannot infer causal direction from data alone  
   - DAGs assume no hidden confounders (unless explicitly modeled)


---

### 1.2 Handling Confounders in Regression on Observational Data

When working with **observational (non-experimental) data**, estimating the causal effect of a variable (e.g., ad spend, feature change) on an outcome (e.g., conversions, sales) is vulnerable to **confounding bias**. To obtain a valid estimate, it's critical to understand what variables to **control for** — and which to avoid.

1. Control for **Confounders**

   Confounders are variables that **influence both the treatment (X)** and **the outcome (Y)**, creating a spurious association.
   
   - **Example**:  
     If you're estimating the effect of **marketing spend** on **sales**, but **seasonality** affects both, seasonality is a confounder.
   
   - **Solution**:  
     Include confounders as covariates in your regression model:
     \[
     Y = \beta_0 + \beta_1 X + \beta_2 Z + \varepsilon
     \]
     where \( Z \) is the confounding variable.
   
   - **Other approaches**:  
     - Propensity score matching or stratification  
     - Inverse probability weighting  
     - Causal forests / ML-based covariate adjustment


2. Do **Not** Control for **Colliders**

   Colliders are variables that are **effects of two variables** (e.g., \( X → Z ← Y \)). Conditioning on a collider opens a backdoor path and introduces **spurious correlation**.
   
   - **Example**:  
     If ad spend and sales both affect “PR buzz,” controlling for buzz will **bias** the estimate of ad spend’s effect on sales.
   
   - **Rule**:  
     **Avoid including colliders** in your regression model. Use a DAG to identify them.

3. Be Careful with **Mediators**
   Mediators lie **on the causal path** from treatment to outcome (e.g., \( X → M → Y \)). Including them **blocks** part of the causal effect.
   
   - **Use case**:
     - **Exclude mediators** if you want the **total effect**
     - **Include mediators** if you want the **direct effect** of X, controlling for M
   
   - **Example**:  
     If ad spend increases awareness, which then increases sales, and you control for awareness, you're estimating the direct (not total) effect of ad spend

**Practical Steps for Regressions on Observational Data**

1. **Draw a causal DAG** to clarify relationships  
2. **Identify and control for confounders** using domain knowledge  
3. **Avoid colliders** or post-treatment variables  
4. **Decide whether to include mediators** based on your goal (total vs direct effect)  
5. **Validate model assumptions** and consider robustness checks

---

### 1.3 Difference-in-Differences (DiD)

Essentially a regression model.
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

### 1.4 Synthetic Control Method

- Used when there’s only **one treated unit** (e.g. one treated city or region) and **multiple potential control units**.
- Builds a **synthetic control group** by creating a weighted average of untreated units that closely matches the treated unit in the **pre-treatment period**.
- Allows estimation of the **counterfactual**: what would’ve happened to the treated unit if there were no intervention.
- **Best for** observational settings where RCTs aren’t possible and you have **long time series data**.
- Assumes **pre-intervention trends** are good predictors of the post-intervention counterfactual.
- Better if DiD's parallel trends assumptions doesn't hold.
- To select control units, Use pearson correlation (r > 0.7), include as many as you can find. P values here is irrelevant since you have autocorrelation anyway because it's a time-series data structure.
- Optional include covariates, so aside from each city conversions data, maybe ctr, impression share, demographics, pricing and other.
- Implementation in Python: `causalimpact` or manual using `R`’s `Synth` package logic.

---

### 1.5 Regression Discontinuity Design (RDD)

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

### 1.6 Instrumental Variables (IV)

- **Purpose**: Estimate causal effects when independent variable is endogenous  
- **Problem**: Endogeneity → correlation between regressor and error term (biases OLS)

- **When to Use IV**
   - Independent variable (X) is endogenous (e.g., due to:
     - Omitted variable bias  
     - Measurement error  
     - Reverse causality)
   - You have an **instrumental variable (Z)** that:
     - Is **correlated** with X (relevance)
     - Affects Y **only through** X (exclusion restriction)

- **Key Variables**
   - **Y**: Outcome variable  
   - **X**: Endogenous independent variable  
   - **Z**: Instrumental variable

**- 2-Stage Least Squares (2SLS)** 
1. **First stage**:  
   `X = π₀ + π₁Z + u`  
   → Get predicted \( \hat{X} \)

2. **Second stage**:  
   `Y = β₀ + β₁ * X̂ + ε`  
   → Estimate causal effect \( β₁ \)

- **Example**
   - Goal: Effect of **education** (X) on **income** (Y)  
   - Instrument: **Distance to college** (Z)  
     - Affects education  
     - Unlikely to directly affect income

- **Assumptions**
   - **Relevance**: \( Cov(Z, X) ≠ 0 \)  
   - **Exclusion Restriction**: \( Cov(Z, ε) = 0 \)  
   - **Monotonicity**: No defiers (for LATE interpretation)
     
- **Limitations**
   - Hard to find strong, valid instruments  
   - **Weak instruments** → biased estimates  
   - Identifies **LATE** (Local Average Treatment Effect), not ATE


---

### 1.7 Propensity Score Matching (PSM)

- Used when treatment and control groups **differ in observed characteristics**, meaning no parallel trends pre-treatment, or if no proper control groups were assigned and maintained during the experiment (for example ran experiment on berlin, but other control cities candidates had multiple interventions at the same time, thus diminishing the parallel trend assumptions, then PSM helps us find the cities that could serve best as control groups).
- Matches each treated unit to similar control unit(s) based on **propensity scores** (probability of receiving treatment given covariates).
- Reduces **selection bias** and simulates randomization in **observational studies**.
- Matching methods: 1:1 nearest neighbor, caliper, kernel matching.
- After matching: analyze treatment effect on matched sample using **t-test, regression, or DiD**.
- Output: balanced dataset with **comparable treated and control units**. For example: Berlin (Treatment) had PS 0.81 will be matched to control cities with similar score only.
- Often used before DiD if there are **no parallel trends** due to covariate imbalance.

---

### 1.8 Bayesian Causal Impact

- A time series method for estimating causal effects when only **one treated unit** exists and traditional control groups or RCTs are not feasible.
- Builds a **Bayesian model** of the treated unit’s pre-treatment behavior to **forecast a counterfactual** (what would’ve happened without treatment).
- Results are presented as **posterior distributions and credible intervals**, offering intuitive uncertainty estimates.

- ✅ **Can be run using only the treatment group's pre-treatment data** (e.g. one year of daily or weekly data preferred for stability).
- ✅ Alternatively, it can incorporate **control units' pre- and post-treatment data** to build a stronger **synthetic control**, allowing analysis with a **shorter pre-period** (as little as 30 days).
- ⚠️ Including covariates (e.g., performance of other cities, traffic, pricing signals) **is optional**, but greatly improves the accuracy of the counterfactual.

- 📈 **Key Advantage over DiD**:
  - Automatically adjusts for **seasonality**, **trend shifts**, and **external noise** through its **Bayesian time series modeling**.
  - Handles time-based dependencies more robustly than traditional DiD, especially in the presence of autocorrelation or volatile baselines.

- 🔧 Implementation:
  - Use `causalimpact` in Python (ported from the original R package).
  - Internally built on **Bayesian Structural Time Series (BSTS)** modeling.

- 💡 Best used for:
  - Evaluating **geo-level campaign impact**, retail experiments, or product launches where only **one treated region or time window** exists.

---

### 1.9 Uplift Modeling

Uplift modeling (a.k.a. incrementality modeling or CATE estimation) predicts the **individual-level effect** of a treatment (e.g. ad, email) on an outcome (e.g. purchase), rather than just the outcome itself.

**Purpose:**  
   
   - Estimate **incremental impact** of a treatment  
   - Identify **who is influenced** by an action  
   - Optimize **targeting, bidding, and suppression**  
   - Maximize **ROAS** by spending only on persuadable users

**How It Works:**

   **Traditional model:** P(Y=1 | X) → likelihood of conversion
   
   **Uplift model:** P(Y=1 | T=1, X) - P(Y=1 | T=0, X) → individual treatment effect (uplift)

      This difference is also called **CATE**: Conditional Average Treatment Effect.

**Types of Uplift Models:**

| Model Type        | Description                                           |
|-------------------|-------------------------------------------------------|
| T-Learner         | Two separate models: one for treated, one for control|
| S-Learner         | One model with treatment as a feature                 |
| X-Learner         | Blends T-learners with re-weighted residuals         |
| Uplift Trees      | Tree splits optimize uplift directly                  |
| Meta-learners     | Advanced estimators (e.g. Doubly Robust, DML, R-Learner) |

**Libraries:**  

| Library          | Highlights                                         |
|------------------|----------------------------------------------------|
| `scikit-uplift`  | Uplift trees, metrics, Qini plots                  |
| `econml`         | Microsoft's causal ML package, supports meta-learners and confidence intervals  
| `causalml`       | Flexible uplift modeling + evaluation              |
| `upliftml`       | Lightweight library with Tree and Forest models, easy to use  
| `grf` (R)        | Generalized Random Forests for uplift              |

**Use `econml` or `scikit-uplift`** if you want serious evaluation, meta-learning, or confidence intervals.

**Data Requirements:** 

   - RCT-style data (randomized treatment assignment)
   - `T` = treatment indicator (1 = treated, 0 = control)
   - `Y` = outcome (binary or continuous)
   - `X` = user features (covariates)


**📈 Use Cases:**

| Scenario                        | Goal                                       |
|----------------------------------|--------------------------------------------|
| Email campaign                  | Target users who convert *because* of email |
| Branded search ads              | Show ads only to users with incremental ROAS |
| Discount/promo offers           | Avoid discounting to sure converters        |
| Retargeting                     | Suppress users unlikely to be influenced    |
| ROAS bidding                    | Predict and use uplift as a bid signal      |


**📊 Evaluation Metrics**

| Metric         | Description                                               |
|----------------|-----------------------------------------------------------|
| Qini Curve     | Measures how well model ranks users by true uplift       |
| Qini AUC       | Area under Qini curve (higher is better)                 |
| Uplift@K       | Incremental gain if top K% scored users are targeted     |
| AUUC           | Area under uplift curve                                  |
| Real-world ROAS| Validate by A/B testing high vs low uplift users         |


**⚠️ Pitfalls to Avoid**

   - Using observational data without adjustment → confounding
   - Evaluating with AUC/accuracy instead of Qini/AUUC
   - Targeting on likelihood of conversion rather than true uplift
   - Not checking business value (e.g. incremental ROAS)

**📊 Feature Importance in Uplift Modeling:**

Feature importance helps identify which variables truly drive **incremental response** — not just overall outcome.

**✅ How Feature Importance Works by Model Type:**
   
   - **T-Learner**  
     Train separate models for treatment and control.  
     → Compare feature influence across both models.  
     → Features important only under treatment may indicate drivers of uplift.
   
   - **Uplift Trees / Forests**  
     Models are built to split users by difference in treatment effect.  
     → Feature importance reflects which variables help separate persuadables, sure things, and lost causes.
   
   - **Meta-Learners (e.g. X-Learner, DR-Learner)**  
     Estimate CATE directly.  
     → Feature importance reflects how much each variable contributes to predicting individual uplift.

**🧠 How to Interpret Feature Importance**

| Feature Behavior               | What It Suggests                             |
|-------------------------------|-----------------------------------------------|
| High in both treatment & control | General driver of behavior (not uplift-specific) |
| High in treatment only         | May influence response to treatment           |
| High in uplift model           | Likely true **causal driver** of uplift       |
| Low importance                 | Not relevant for outcome or response          |

**📌 Usefulness**
   
   - Focus targeting and bidding strategies on high-uplift segments
   - Identify variables that truly impact **incremental conversions**
   - Avoid wasting spend on segments already likely to convert

**⚠️ Caution**
   
   - Feature importance ≠ causality unless uplift is modeled correctly  
   - Must be based on RCT data to trust causal signals  
   - Always pair with domain knowledge and experiment results


**🤔 Uplift vs. Causal Impact**

| Use Case                         | Recommended Method    |
|----------------------------------|------------------------|
| Aggregate campaign lift          | Causal Impact (time series) |
| Geo-level intervention           | Causal Impact          |
| Predict per-user treatment effect| Uplift Modeling        |
| Optimize individual targeting    | Uplift Modeling        |
| You have time series, not RCT    | Causal Impact          |
| You have RCT with covariates     | Uplift Modeling        |


**✅ Summary**  

Uplift modeling answers:

> “Who is influenced by the treatment — and should therefore be targeted?”

It helps marketing teams make **causal, cost-effective** decisions at the **user or segment level**.


---


### 1.10 4-Cell RCT with Holdout Cells for Incrementality Testing

   A **4-cell randomized controlled trial (RCT)** with a **holdout group** is a clean experimental design used to measure both **incremental effects** and **baseline trends**.
   
   **Design Structure**
   
   | Group       | Treatment | Measurement |
   |-------------|-----------|-------------|
   | **1. Exposed Group (Test)**      | ✅ Yes    | ✅ Yes        |
   | **2. Measurement-Only Group**    | ❌ No     | ✅ Yes        |
   | **3. Treatment-Only Group**      | ✅ Yes    | ❌ No         |
   | **4. Holdout (Pure Control)**    | ❌ No     | ❌ No         |
   
   **Purpose of Each Group**
   
   - **Group 1 (Exposed & Measured)**: Measures the actual effect of the treatment  
   - **Group 2 (Not Treated, Measured)**: Captures baseline behavior without treatment  
   - **Group 3 (Treated, Not Measured)**: Prevents measurement bias (e.g. Hawthorne effect)  
   - **Group 4 (Pure Holdout)**: Used to test for contamination or as a long-term baseline
   
   **Benefits**  
   - Isolates **treatment effect** from **observation effect**  
   - Enables testing for **measurement bias**
   - Adds robustness to **incrementality analysis**
   
   **📊 Use Cases**  
   - Digital advertising (incrementality of impressions)
   - UX or messaging experiments (measuring observation effects)
   - Geo-experiments with partial exposure
   
   **📌 Example Interpretation**  
   - To estimate the **true causal effect**, compare Group 1 vs. Group 2.  
   - To detect **measurement bias**, compare Group 2 vs. Group 4.
   
---

## 2. Regression Models

### 2.1 Simple Linear Regression
- Predicts a **continuous outcome** based on one independent variable.
- Fits a line that **minimizes Mean Squared Error (MSE)**.
- Assumes:
  - **Linearity**: Relationship between X and Y is linear
  - **Independence**: Observations are independent
  - **Homoscedasticity**: Constant variance of errors
  - **Normality**: Errors are normally distributed
- Common metrics:
  - Coefficient of determination (**R²**): proportion of variance explained
  - **Standard Error**: measures spread of residuals
  - **t-test**: used to test significance of slope coefficient

---

### 2.2 Multiple Linear Regression
- Predicts a continuous outcome from **two or more predictors**.
- Same assumptions as simple regression, plus:
  - **No multicollinearity**: predictors shouldn’t be too highly correlated
    - Check using **Variance Inflation Factor (VIF)** and **Tolerance**
- Coefficients:
  - **Unstandardized**: raw units (e.g., € per click)
  - **Standardized**: unitless, comparable across predictors
- Model evaluation:
  - **R² / Adjusted R²**: adjusted accounts for number of predictors
  - **F-test**: tests if the model explains a significant portion of the variance
- Use **dummy variables** for categorical features:
  - Drop one level as a baseline to avoid the dummy variable trap

---

### 2.3 Logistic Regression
- Used for **binary classification problems** (e.g., conversion: yes/no)
- Models the **probability** of success using a **sigmoid (logit) function**
- Unlike linear regression, it uses:
  - **Maximum Likelihood Estimation (MLE)** instead of least squares
- Output:
  - **Odds ratio** for interpretation of coefficients
  - **Log loss** as an evaluation metric
- Assumptions:
  - Linearity in the **log odds**, not in Y itself
  - Independence of observations
  - No multicollinearity
- Inference:
  - **Wald’s z-test** and **Likelihood-Ratio (Chi-squared) test** used to assess predictor significance
- Extensions:
  - **Multinomial Logistic Regression**: for 3+ outcome classes
  - **Regularized Logistic Regression**: includes L1 (Lasso) or L2 (Ridge) penalties

---

## 3. Choosing & Designing the Right Causal Method

### 🎯 Goal

Estimate the **causal effect** of a treatment (e.g., ad campaign, feature change) on an outcome (e.g., conversions, revenue), using the **best method for your data and experimental setup**.

Avoid:
- Confounding bias
- Selection bias
- Time-based noise (seasonality, trend shifts)
- Misinterpretation of correlation as causation



### 🧭 Core Causal Method Flow: DiD → PSM → Causal Impact

#### Step 1: Do You Have Pre & Post Treatment Data?
- ✅ Yes → Start with **Difference-in-Differences (DiD)**

#### Step 2: Check Pre-Treatment Trends
- Do treated and control units have **parallel trends** before the intervention?
  - ✅ Yes → Use **DiD**
  - ❌ No → Apply **Propensity Score Matching (PSM)** to rebalance covariates

#### Step 3: After PSM, Check Again
- Do you now have **balanced pre-trends**?
  - ✅ Yes → Use **DiD on matched sample**
  - ❌ No → Use **Bayesian Causal Impact** or **Synthetic Control**


#### 🔁 Summary of Flow
Pre/Post Data → DiD → Trends Misaligned → PSM → Still Misaligned? → Bayesian Causal Impact / Synthetic Control

### 🧠 When to Use Each Method

#### ✅ Difference-in-Differences (DiD)
- **Use when**: Treated + control groups with parallel pre-trends
- **Pros**: Simple, robust if assumptions hold
- **Cons**: Fails if trends are not parallel

#### ✅ Propensity Score Matching (PSM)
- **Use when**: Treated/control groups differ in covariates
- **Goal**: Match units to simulate randomization before applying DiD

#### ✅ Bayesian Causal Impact (CI)
- **Use when**: You have **only 1 treated unit** or can't meet DiD assumptions
- **Mechanism**: Forecasts counterfactual using **Bayesian time-series model**
- **Pros**: Adjusts for seasonality, trends, and noise
- **Cons**: Requires solid pre-period and predictive control variables

### 🧪 Uplift Modeling: When to Include It?

| Role in causal analysis         | Not used to measure overall treatment effect |
|----------------------------------|----------------------------------------------|
| Used for                         | **Optimizing individual targeting**          |
| Requires                         | RCT / A/B test (user- or geo-level)          |
| Measures                         | **Incremental effect per individual or segment** |
| Output                           | "Who will respond positively to treatment"   |
| Analysis level                   | Micro (user-level), not macro                |

**Use it when:**
- You already ran an A/B test or geo experiment  
- You want to **target future campaigns more efficiently**  
- You care about **incremental ROAS at the user level**, not just overall lift


### 🧠 Method Selector: Comparison Table

| Scenario                                     | DiD | PSM + DiD | Bayesian CI | RDD | Uplift Modeling |
|----------------------------------------------|-----|------------|-------------|-----|------------------|
| Treated & control groups available           | ✅  | ✅         | ❌          | ❌  | ✅ (post-test)   |
| Control group not parallel pre-treatment     | ❌  | ✅         | ✅          | ❌  | ✅ (if RCT)      |
| Only one treated unit (e.g. geo)             | ❌  | ❌         | ✅          | ❌  | ❌               |
| Pre/post time series exists                  | ✅  | ✅         | ✅          | ❌  | ❌               |
| Randomized treatment (A/B or geo test)       | ✅  | ✅         | ✅          | ❌  | ✅               |
| Treatment assigned by threshold              | ❌  | ❌         | ❌          | ✅  | ❌               |
| Need to model individual treatment effects   | ❌  | ❌         | ❌          | ❌  | ✅               |
| Need uncertainty/credible intervals          | ❌  | ❌         | ✅          | ❌  | ❌               |

---

#### 🧪 Experiment Design → Data Structure → Method Template

| Step                        | Questions to Ask                                  | Leads To                              |
|-----------------------------|----------------------------------------------------|----------------------------------------|
| **Design**                  | Can I randomize treatment?                         | Yes → A/B or Geo test                 |
|                             | No → Use observational methods                     |                                        |
| **Data Structure**          | Do I have pre/post panel data?                     | Yes → Try DiD                         |
|                             | Is control imbalanced or not parallel?             | Use PSM or move to Causal Impact      |
|                             | Only 1 treated unit?                               | Use Bayesian Causal Impact            |
|                             | Treatment threshold rule?                          | Use RDD                               |
| **Output Needs**            | Do I need user-level predictions?                  | Use Uplift Modeling (with A/B design) |
|                             | Want overall campaign lift + confidence intervals? | Use Bayesian CI                       |
|                             | Want interpretable effect on metric Y?            | Use DiD or regression                 |


#### 🧠 CI vs Uplift — Key Distinction

| Metric                     | Causal Impact             | Uplift Modeling                        |
|----------------------------|---------------------------|----------------------------------------|
| Level of analysis          | Macro (geo, campaign)     | Micro (user or segment)                |
| Output                     | Total lift over time      | Incremental effect per user            |
| Use case                   | Did the campaign work?    | Who should we target next time?        |
| Needs experimental design? | Not strictly              | ✅ Must be RCT                          |
| Needs long pre-period?     | ✅ Yes                    | ❌ No (just post-experiment data)       |

---

### 4. Example Analyses for Paid Search & How to Do Them

| Analysis Goal                                               | Example Question                                                                 | Method(s) to Use                         | Notes                                                                                   |
|-------------------------------------------------------------|----------------------------------------------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------|
| Measure impact of branded search spend                      | Do branded keywords actually drive incremental bookings?                         | Geo A/B Test + DiD or Causal Impact       | Run geo holdout; analyze post-period booking deltas or use CI with untreated cities     |
| Estimate incremental ROAS from search campaigns             | Is our branded campaign delivering >1.5x ROAS incrementally?                     | Causal Impact or Geo Test + ROAS calc     | Include ad spend and revenue; CI gives credible intervals for effect                    |
| Optimize who sees branded ads                               | Which users should see our branded ads to maximize efficiency?                   | Uplift Modeling (T-learner, X-learner)    | Requires RCT; use to segment future users by expected uplift                            |
| Evaluate effectiveness of new bidding strategy              | Did switching to a new bidding algorithm improve bookings or ROAS?               | DiD or Causal Impact                      | Use control group on old bidding strategy; ensure pre-period trends are parallel        |
| Quantify lift from a promo extension in ads                 | Did including “10% off” in search ads increase conversions?                      | A/B Test or Geo Test + DiD                | Split regions or campaigns; compare conversion rates and value                          |
| Diagnose campaign saturation or waste                       | Are we overspending on users who would convert anyway?                           | Uplift Modeling + ROAS Threshold Filtering| Predict incremental ROAS; suppress low or negative uplift users                         |
| Justify spend on awareness/upper funnel keywords            | Do generic search terms lead to eventual bookings in exposed markets?            | Geo Test + Causal Impact                  | Use long attribution windows; CI captures delayed lift                                  |
| Analyze cannibalization between paid and organic            | If we pause branded search, do users book anyway via organic?                    | Geo A/B Test + DiD or CI                  | Requires careful measurement of both paid and organic traffic during test               |
| Forecast post-campaign booking drop-off                     | What happens when we turn off branded campaigns?                                 | Causal Impact (time series forecasting)   | Predict counterfactual; compare actual drop-off vs. forecasted baseline                 |
| Estimate effect of spend level change (e.g. +20%)           | What’s the causal effect of increasing branded search budget in top cities?      | Instrumental Variable (if spend endogenous) or Geo Split + DiD | Use IV only if randomization is infeasible and you have valid instruments              |

#### 📊 Essential Non-Causal Analyses for Paid Search Optimization

| Analysis Goal                                           | Example Question                                                             | Method(s) to Use                       | Notes                                                                 |
|---------------------------------------------------------|------------------------------------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------|
| Optimize Quality Score                                  | What are the key drivers of Quality Score drops across branded campaigns?   | Multiple Linear Regression             | Use CTR, Ad Relevance, Landing Page Experience as predictors         |
| Improve cost-efficiency across segments                 | Which campaigns or geos deliver high CPC but low ROAS?                      | Aggregated ROAS & CPA benchmarks       | Regularly refresh dashboards and flag underperformers                 |
| Understand bid landscape behavior                       | How does CPC behave when impression share or budget changes?                | Bid Landscape Analysis + Correlation   | Use daily/weekly time series to find thresholds or diminishing returns|
| Forecast performance based on budget scenarios          | What will happen if we cut or increase branded budget by 20%?               | Scenario Forecasting (linear or logistic) | Use historical data to model nonlinear spend-to-revenue behavior    |
| Track and attribute upper-funnel keyword contribution   | Do generic search terms indirectly lead to conversions later?               | Assisted Conversion Tracking / Path Analysis | Use Google Analytics, GA4, or attribution models                     |
| Optimize ad text performance                            | Which headline or description variations have the best CTR or CR?           | A/B Testing + CTR/CR comparisons       | Use ad variations at ad group level with sufficient volume            |
| Segment campaign performance by audience/device         | How do branded campaigns perform differently on mobile vs. desktop?         | Segmentation Analysis + Pivoting       | Use GA and ad platform segmentation filters                           |
| Identify seasonality or cyclicality in branded search   | When does branded traffic spike or dip across markets?                      | Time Series Decomposition              | Use STL or moving averages to isolate trend, seasonality, and noise  |
| Correlate branded demand with external factors          | Do holidays, events, or weather impact search volume and conversion?        | External Data Join + Correlation       | Use calendar or 3rd-party datasets and blend with search trends       |
| Benchmark GYG against competitors on branded terms      | Are competitors consistently bidding on our branded keywords?               | Auction Insights + Share of Voice      | Review impression share, overlap rate, and position vs. competition   |

---

## 5. Design of Experiments (DoE)

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

## 6. libraries  

   **7.1 General Regression-Based Causal Inference**
      - `statsmodels`
        - OLS, logistic regression, DiD, fixed effects
        - Covers most classical regression-based causal techniques
      
      - `linearmodels`
        - Advanced panel data support (fixed/random effects, IV, DiD variants)
        - Better than `statsmodels` for complex panel setups



   **7.2 Uplift Modelling, Meta-Learners & CATE Estimation**
        - `econml` (by Microsoft)
        - Meta-learners: S-, T-, X-, R-, DR-Learner
        - Supports uplift modeling, IVs, and doubly robust estimation
        - Causal forest, orthogonal random forests, confidence intervals
        - Best for user-level treatment effect estimation
      
      - `CausalML` (by Uber)
        - T-, S-, X-learners
        - Supports uplift scoring, causal forest, XGBoost + CATE
        - Easier than `econml` for quick uplift tasks
      
      - `scikit-learn`
        - Not causal-specific, but used as a base for learners in `econml`, `causalml`, and uplift modeling pipelines

      - `scikit-uplift`
        - Uplift random forest, uplift trees
        - Evaluation tools: Qini curves, uplift@K, AUUC
        - Great for clean, purpose-built uplift modeling
      
      - `upliftml`
        - Simpler uplift tree models with fast implementation
        - Good lightweight alternative

   **7.3 Time Series Causal Inference**
      - `causalimpact`
        - Bayesian structural time series for estimating causal effect of interventions
        - Ported from Google’s R package to Python
        - Ideal for single treated unit with long pre-period (e.g. one geo)
      
      - `prophet`
        - Not causal-specific, but useful for creating pre-period forecasts (e.g. to manually approximate counterfactuals)

   **7.4 Causal Graphs & Identifiability**
      - `DoWhy`
        - DAG creation and causal reasoning using structural assumptions
        - Supports identifiability, backdoor/IV criteria, and refutation
        - Integrates with `econml` for estimation
      
      - `causalnex`
        - DAG-based learning from data
        - Bayesian Network-based structure modeling
        - Focus on business decision modeling, not just identifiability

      - `dagitty` (web tool)
        - Browser-based DAG editor and backdoor identification
        - Not a Python lib, but crucial in causal workflow

   **7.5 Matching & Propensity Scores**
      - `pymatch`
        - Simple API for propensity score matching
        - Can do nearest-neighbor matching, caliper, diagnostics
        - Great for balancing observational data before DiD
      
      - `causalml` and `DoWhy`
        - Also support PSM internally (no need for `pymatch` alone)

   **7.6 Bayesian Modeling (Advanced)**
      - `PyMC` / `pymc3` / `pymc`
        - Probabilistic programming for full Bayesian modeling
        - Use when you want posterior distributions, custom priors, or full probabilistic causal analysis
        - Can be used for Bayesian IVs, Bayesian regression, or custom synthetic controls
      
      - `bambi`
        - High-level wrapper around PyMC for Bayesian regression (like `statsmodels` but Bayesian)
        - Useful for rapid prototyping of Bayesian GLMs


---
