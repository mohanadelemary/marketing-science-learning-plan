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
