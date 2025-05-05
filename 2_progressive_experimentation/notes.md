# **2. Progressive Experimentation: Causal, DiD, Geo Tests & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

## 📘 Index

1. [Causal Inference](#causal-inference)  ❌  
   1.1. [Difference-in-Differences (DiD)](#11-difference-in-differences-did)  
   1.2. [Synthetic Control Method](#12-synthetic-control-method-) ✅  
   1.3. [Regression Discontinuity Design (RDD)](#13-regression-discontinuity-design-rdd)  
   1.4. [Instrumental Variables (IV)](#14-instrumental-variables-iv)  
   1.5. [Propensity Score Matching](#15-propensity-score-matching)  
   1.6. [Uplift Modeling](#16-uplift-modeling)  
   1.7. [Causal Diagrams & DAGs](#17-causal-diagrams--dags)  
   1.8. [Bayesian Causal Impact](#18-bayesian-causal-impact)

2. [Geo Experiments & Geo Lift Analysis](#geo-experiments--geo-lift-analysis)  ❌  
   2.1. Aggregate Geo-Based A/B Tests  
   2.2. Pre/Post Trends and Control Matching  
   2.3. Applications for Brand/Media Testing  

3. [Regression Models](#regression-models)  ❌  
   3.1. Simple Linear Regression  
   3.2. Multiple Linear Regression  
   3.3. Logistic Regression  

4. [Choosing & Designing the Right Causal Method](#choosing--designing-the-right-causal-method)  ❌  

5. [Design of Experiments (DoE)](#design-of-experiments-doe)  ❌  

6. [Libraries](#libraries) ❌  
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

## Causal Inference

### 1.1 Difference-in-Differences (DiD)
_TODO: Add theory and assumptions._

### 1.2 Synthetic Control Method
_TODO: Add summary and applied notes._

### 1.3 Regression Discontinuity Design (RDD)
_TODO: Add theory and implementation tips._

### 1.4 Instrumental Variables (IV)
_TODO: Add assumptions, 2SLS and examples._

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

## Choosing & Designing the Right Causal Method

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



