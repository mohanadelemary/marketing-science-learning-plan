# **2. Causal Inference & Regression Modeling**

> Goal: Move beyond correlation and estimate treatment effects in both experimental and observational settings.

### 📘 Topics:

- **Causal Inference**
    - **Difference-in-Differences (DiD)**
    - **Synthetic Control Method** ✅
    - Regression Discontinuity Design (RDD)
    - Instrumental Variables (IV)
    - Propensity Score Matching
    - Uplift modeling (individual-level treatment effect estimation)
- **Regression Models**
    - OLS, Logistic Regression
    - Fixed Effects, Clustered SEs
    - Interaction terms

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
