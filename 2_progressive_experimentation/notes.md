# **2. Progressive Experimentation: Causal, DiD, Geo Tests & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

## 📘 Index

1. [Causal Inference](#causal-inference)  
   1.1. [Difference-in-Differences (DiD)](#11-difference-in-differences-did)  
   1.2. [Synthetic Control Method](#12-synthetic-control-method-) ✅  
   1.3. [Regression Discontinuity Design (RDD)](#13-regression-discontinuity-design-rdd)  
   1.4. [Instrumental Variables (IV)](#14-instrumental-variables-iv)  
   1.5. [Propensity Score Matching](#15-propensity-score-matching)  
   1.6. [Uplift Modeling](#16-uplift-modeling)  
   1.7. [Causal Diagrams & DAGs](#17-causal-diagrams--dags)  
   1.8. [Bayesian Causal Impact](#18-bayesian-causal-impact)

2. [Geo Experiments & Geo Lift Analysis](#geo-experiments--geo-lift-analysis)  
   2.1. Aggregate Geo-Based A/B Tests  
   2.2. Pre/Post Trends and Control Matching  
   2.3. Applications for Brand/Media Testing  

3. [Regression Models](#regression-models)  
   3.1. Simple Linear Regression  
   3.2. Multiple Linear Regression  
   3.3. Logistic Regression  

4. [Choosing & Designing the Right Causal Method](#choosing--designing-the-right-causal-method)

5. [Design of Experiments (DoE)](#design-of-experiments-doe)

6. [Libraries](#libraries)  
7. [Notes & Summaries](#notes--summaries)  
8. [Resources](#resources)

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

### 1.2 Synthetic Control Method ✅
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

## Libraries

- `statsmodels` (OLS, logistic, fixed effects, DiD)
- `econml` (CATE estimation, uplift modeling, IVs, meta learners)
- `DoWhy` (causal graphs, identifiability, backdoor criteria)
- `causalimpact` (Bayesian time series intervention model, ported from R to Python)
- `PyMC`, `pymc3` (Bayesian modeling, priors, posteriors)
- `scikit-learn` (base regression models, preprocessing)
- `CausalML` (uplift models: S-learner, T-learner, X-learner)

## Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here.

## Resources

- [ ] PYMC-Marketing https://www.youtube.com/watch?v=RY-M0tvN77s  
- [ ] Bayesian Marketing Science https://www.youtube.com/watch?v=5QgiixYjmTM&t=1320s
























# **2. Progressive Experimentation: Causal, DiD, Geo Tests & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

### 📘 Topics:

- **Causal Inference**
    - **Difference-in-Differences (DiD)**
    - **Synthetic Control Method** ✅
    - Regression Discontinuity Design (RDD)
    - Instrumental Variables (IV)
    - Propensity Score Matching
    - Uplift modeling (individual-level treatment effect estimation)

Geo Experiments & Geo Lift Analysis
5.1. Aggregate Geo-Based A/B Tests
5.2. Pre/Post Trends and Control Matching
5.3. Applications for Brand/Media Testing

- **Regression Models**
    - OLS, Logistic Regression
    - Fixed Effects, Clustered SEs
    - Interaction terms
 Regression ✅ 6.1. Simple Linear Regression
6.2. Multiple Linear Regression
6.3. Logistic Regression
  

### 🧰 Libraries:

- `statsmodels` (OLS, logistic, fixed effects, DiD)
- `econml` (CATE estimation, uplift modeling, IVs, meta learners)
- `DoWhy` (causal graphs, identifiability, backdoor criteria)
- `causalimpact` (Bayesian time series intervention model, ported from R to Python)
- `PyMC`, `pymc3` (Bayesian modeling, priors, posteriors)
- `scikit-learn` (base regression models, preprocessing)
- `CausalML` (uplift models: S-learner, T-learner, X-learner)

## 📓 Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here.

## 🔗 Resources

- [ ] Add articles, blogs, papers, videos, or documentation here.
- [ ] PYMC-Marketing  https://www.youtube.com/watch?v=RY-M0tvN77s
- [ ] Bayesian Marketing Science https://www.youtube.com/watch?v=5QgiixYjmTM&t=1320s




### 🔍 Common Tests Behind Causal Inference Techniques

| Method                        | What's Actually Tested                              | Under-the-Hood Test              |
|------------------------------|------------------------------------------------------|----------------------------------|
| **A/B Testing (RCT)**        | Mean difference between groups                      | **t-test** or **z-test**         |
| **Difference-in-Differences**| Pre-post changes across groups                      | **Regression + t-test**          |
| **Regression Analysis**      | Coefficient of treatment variable ≠ 0               | **t-test on β coefficient**      |
| **Propensity Score Matching**| Mean outcome difference post-matching               | **t-test** / **non-parametric**  |
| **Instrumental Variables**   | Effect of instrument on outcome (2SLS)              | **t-test** on 2SLS regression    |
| **CausalImpact**             | Post-treatment deviation from expected trend        | **Bayesian posterior test**      |
| **Uplift Modeling**          | Differential treatment effect per individual        | **Model-based; may test uplift > 0** |


____________________________________________________________________________________________________________________________________


Regression
Simple Linear Regression
Linear equation that you solve for by minimizing the MSE or others like ASE.
Assumptions in SLR to be checked before interpreting the regression results:

Relationship can be fitted by a straight line
Independence of errors. the error between real and predicted values for one value doesnt's influence the error for others
Homoscedasticity: If resdiuals are plotted on a y-axis along the predicted values on x-axis, they should be evenly distributed across the plane and not for exampleincrease as the predicted values on the x-axis increase like a funnel shape (heteroscedasdticity)
Errors follow a normal distribution (analytical normality tests or Q-Q plots)
Multiple Linear Regression
Assumptions in MLR to be checked before interpreting the regression results:

The four assumptions in SLR Plus one more: - No Multi-Collinearity: MC is when two or more predictor variables are highly correlated. hard to assign weights due to info overlap.
MC is not a massive issue if we just want to predict with the model, but it is if the goal is interpret the influence of predictor variables.
We determine the R-squared value for each predictor variable. High r-sq. means the variable's variance is higly explained by the other predictor variables.
From there, we calculate Tolerance and VIF for the variables. VIF measures how much the variance of a regression coefficient is inflated due to multicollinearity (correlation among predictors).
Treatment of MC: consider removing high MC variable or combining variables.
MLR summary

Unstandardized coefficient per variable are what's used in the equation but handles multiple units of variables
Standardized coefficients are standardized among units and sclaes, giving a more standardized and fair way to evaluate the influence and importance of each variable in the regression.
R = Correlation
R-Squared = shows how well is the variance in the predicted value explained by model
Adjusted R-Squared = Accounts for the number of independent variables in the model. a more accurate measure of explanatory power. if model has too many predictors - regular r-sq could overestimate the power, therefore adjusted r-sq. is then recommended.
Standard error: average distance between line and observed data
Dummy Variables:

If you one-hot encode categories, you drop one of the new variables and use as reference only
Logistic Regression
To classify data rows into binary outputs (0 and 1)
For this we use the logistic function that outputs values between zero and one.
You solve for it using maximum likelihood estimation.
Outputs probability of an event between 0 and 1. based on the threshold you define (usually 0.5) you can make a prediction.
You get coefficients and p-values
You test for statistical significance by wald's z-test or chi-squared (unlike t-statistic for lin reg)
You also get r2 values from multiple variations to determine if the model explains the variablitiy in the predicted variable.



ChatGPT said:
Fantastic — you’re asking the right kind of “under the hood” question. Let’s break down what powers causal inference under the surface: the theoretical foundations, assumptions, and methods that go beyond just running regressions.

🧠 What’s Really Under the Hood in Causal Inference?
At the core of causal inference are three pillars:

1. Counterfactual Thinking (Rubin Causal Model)
What would have happened to this same unit if it had received a different treatment?

This gives us the potential outcomes framework:

For individual 
𝑖
i, we define:

𝑌
𝑖
(
1
)
Y 
i
​
 (1) = outcome if treated

𝑌
𝑖
(
0
)
Y 
i
​
 (0) = outcome if not treated

The causal effect is:

Treatment Effect
𝑖
=
𝑌
𝑖
(
1
)
−
𝑌
𝑖
(
0
)
Treatment Effect 
i
​
 =Y 
i
​
 (1)−Y 
i
​
 (0)
But we only ever observe one of these → this is the fundamental problem of causal inference.

2. Assumptions to Identify Causality
Causal inference is about making identifying assumptions to estimate unobservable counterfactuals. Some common ones:


Assumption	Purpose
Ignorability / Conditional Independence	No unmeasured confounders (e.g., after controlling for X, treatment is as good as random)
Overlap / Positivity	Everyone has a non-zero chance of getting treatment or control
Stable Unit Treatment Value (SUTVA)	One unit’s outcome doesn’t depend on others' treatments (no interference)
Exclusion Restriction	In IV methods: instrument affects outcome only through the treatment
3. Causal Estimation Methods
Each method answers: how can we isolate the causal effect, given what we know?

a) Randomized Controlled Trials (RCTs)
The gold standard.

Treatment is randomly assigned → no confounding.

b) Matching / Propensity Scores
Match treated and control units with similar characteristics.

Balance covariates to simulate a randomized experiment.

c) Regression (with control variables)
Estimate average treatment effect, assuming no omitted variables.

d) Instrumental Variables (IV)
Use a third variable (instrument) that affects treatment but not the outcome directly.

Handles endogeneity and unobserved confounding.

e) Difference-in-Differences (DiD)
Compares before/after changes in treated vs. control groups.

Assumes parallel trends in absence of treatment.

f) Regression Discontinuity (RD)
Uses a cutoff (e.g. age ≥ 65) for assigning treatment.

Units near the threshold are assumed similar.

g) Causal Diagrams / Directed Acyclic Graphs (DAGs)
Visualize and reason about causality.

Help identify which variables to control for.

🔧 Technical Tools Used
Potential Outcomes notation: 
𝑌
(
1
)
,
𝑌
(
0
)
Y(1),Y(0)

Bayesian or frequentist estimation

Structural equation modeling (in some frameworks)

Do-calculus (Judea Pearl's formal rules to manipulate DAGs and identify causal paths)

🧠 Summary: What Powers Causal Inference?

Component	What It Does
Counterfactuals	Frame the problem: what "would have happened"?
Identification assumptions	Allow causal effects to be estimated from data
Estimation methods	Translate theory into actual models
Causal diagrams (DAGs)	Clarify relationships and spot confounding
Would you like me to build a visual DAG example showing how causal inference avoids confounding vs. naive regression? Or maybe a cheat sheet of methods matched to real-world examples?
