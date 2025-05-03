
----------------------------------------------------------
Correlation:

- Goal is to determine strength and direction of correlation (usually a value between -1 to 1)

Pearson Correlation Coefficient (r)
* Null: no corr, alt:corr
* r tells us the corr, running a t-test tells us if r is significantly different from zero.
* Assumptions:
  - Only works on metric variables
  - only detects linear relationships, non-linear relationships won't be detected
  - If we're using r to test a hypothesis (corr. is statistically significant larger than zero, the two variables must be normally distributed.


Spearman Correlation Coefficient (rs)
* non-parametric equivalent of pearson correlation coeff (assign ranks rather than raw numbers).
* Spearman is equal to pearson when done on ranks.

Kendall's tau
* Non-parametric equivalent of pearson correlation and variables need to only have ordinal scale levels (numerical or ordinal but not nominal)
* Exactly the same as spearman but should be preferred over spearman if very few data with many rank ties available

Point-Biserial Correlation Coefficient (rpb)
* A special case of pearson correlation. Examines relationship between dichotomous variable and a metric variable.
* Dichtomous variable is a nominal one with two values (gender M/F, smoking Y/N, etc.), metric varibale is like age, weight, salary
* provides same p-value as an independent t-test
* to test statistical significance of this correlation, metric variable must be normally distributed, otherwise t-value and p-value can't be reliably interpreted.

Conditions to prove Causality
1. Strong and statistically signifcant correlation coefficient
2. Proof of sequence, this can be done in 3 ways:
   a. chronological sequence of events (variable A then B) so variable B results happened after variable A happened.
   b. A controlled experiment in which the two variables can specifically influenced
   c. Strong Theory on how the direction of the relationship goes.
___________________________________________


___________________________________________
Regression

**Simple Linear Regression**

- Linear equation that you solve for by minimizing the MSE or others like ASE

Assumptions in SLR to be checked before interpreting the regression results

1. Relationship can be fitted by a straight line
2. Independence of errors. the error between real and predicted values for one value doesnt's influence the error for others
3. Homoscedasticity: If resdiuals are plotted on a y-axis along the predicted values on x-axis, they should be evenly distributed across the plane and not for exampleincrease as the predicted values on the x-axis increase like a funnel shape (heteroscedasdticity)
4. Errors follow a normal distribution (analytical normality tests or Q-Q plots)

**Multi Linear Regression**

Assumptions in MLR to be checked before interpreting the regression results
- The four assumptions in SLR Plus one more:
- No Multi-Collinearity: MC is when two or more predictor variables are highly correlated. hard to assign weights due to info overlap.
- MC is not a massive issue if we just want to predict with the model, but it is if the goal is interpret the influence of predictor variables.
- We determine the R-squared value for each predictor variable. High r-sq. means the variable's variance is higly explained by the other predictor variables.
- For there, we calculate Tolerance and VIF for the variables.
- Treatment of MC: consider removing high MC variable or combining variables.

MLR summary

- Unstandardized coefficient per variable are what's used in the equation but handles multiple units of variables
- Standardized coefficients are standardization giving a more standardized and fair way to evaluate the influence and importance of each variable in the regression.
- R = Correlation
- R-Squared = shows how well is the variance in the predicted value explained by model
- Adjusted R-Squared = Accounts for the number of independent variables in the model. a more accurate measure of explanatory power. if model has too many predictors - regular r-sq could overestimate the power, therefore adjusted r-sq. is then recommended.
- Standard error: average distance between line and observed data
- 

Dummy Variables:

- If you one-hot encode categories, you drop one of the new variables and use as reference only

________________________________________________

Logistic Regression

- To classify data rows into binary outputs (0 and 1)

- For this we use the logistic function that outputs values between zero and one.
- You solve for it using maximum likelihood estimation.
- Outputs probability of an event between 0 and 1. based on the threshold you define (usually 0.5) you can make a prediction.
- You get coefficients and p-values
- You test for statistical significance by wald's z-test or chi-squared (unlike t-statistic for lin reg)
- You also get r2 values from multiple variations to determine if the model explains the variablitiy in the predicted variable.

________________________________________________
   
Confidence Intervals (Freq.) and Credible Interval (Bayesian)

Right way to define confidence level of 95%: If we keep getting samples, we know that 95% of the samples extracted will contain the population mean
______________________

DOE like full factorial and fractional factorial design
also power analysis and sample size and minimum effect required

________________________________________________

Survival Time Analysis

Statistical analyses concerned with analyzing how much time runs out until a certain event takes place.

Example: analyzing how a person dies after being diagnosed by a disease, or time to retunr to work afterburnout leave.


Goals of survival analysis:

1. Estimate time until an event occurs (e.g. churn, failure, death) (what is robability of event X at time t)
2. Handle censored data (subjects that haven’t experienced the event yet)
3. Compare time-to-event across groups (e.g. treatment vs. control)
4. Model the effect of variables on event timing (via hazard rates)
5. Calculate survival probabilities over time 
𝑆
(
𝑡
)
S(t)
6. Identify risk factors influencing event likelihood (Cox regression)


3 Main things to know: Kaplan Meier Curve, Log Rank Test, Cox Regression

Kaplan Meier Curve

- time on x-axis
- survival rate on y-axis (1 at top, 0 at bottom)
- Example at t 5years, survival rate is 0.7. which means at t5, there's a 70% chance events hasn't occured yet.
- Kaplan Meier Curves Do censoring for data (very unique): Where it partially accounts for events that happen before or after the observation time period, unlike a regression model which would just ignore the data point.


Two tests for testing effect on KM curves
- Log rank to see if there's a diff in KM curver when changing a variale across two camples. cox regression if you're also testing for influence of more variables

🔍 Key Differences Between Log-Rank Test and Cox Regression

Feature	Log-Rank Test	Cox Proportional Hazards Regression
Goal	Test if two or more survival curves are significantly different	Estimate the effect of covariates (like age, channel) on survival time
Type of test	Non-parametric (no assumptions about the shape of survival curves)	Semi-parametric (assumes proportional hazards)
Input	Group/category (e.g. Group A vs. Group B)	Continuous or categorical predictors
Output	A p-value (tests for difference between groups)	Hazard ratios + coefficients for each variable
Adjust for covariates?	❌ No	✅ Yes
Effect size?	❌ No — tells if curves differ, not by how much	✅ Yes — tells how much each variable increases/decreases hazard
Assumes proportional hazards?	✅ Yes	✅ Yes
Visual companion	Kaplan-Meier curves	Can also be plotted as survival curves by covariate
🧠 Summary in Plain Terms:
🧪 Log-Rank Test:
Used when comparing two or more survival curves

Answers: "Are the survival experiences in these groups statistically different?"

No control for other variables

📈 Cox Regression:
Used when modeling how multiple variables affect survival

Answers: "How does each variable (e.g. age, ad channel, platform) impact the risk of event over time?"

Adjusts for multiple covariates and gives hazard ratios (interpretable effect sizes)

✅ When to Use:
Use Log-Rank Test for:

A/B test-style comparisons

Simple group comparisons (e.g., churn rate by user group)

Use Cox Regression for:

Real-world modeling with multiple influencing factors

Need for interpretation (how much faster/slower people churn, die, convert, etc.)


---------------------------------------------------------------------------------------------


**📊 Control Chart – Key Points**
Purpose: Monitor process stability over time
Used for: Detecting unusual variation (signal vs. noise)
Tracks: Metric over time (e.g. conversion rate, ROAS, defects)

📐 Components
- Center Line (CL): Process average
- UCL / LCL: Control limits = mean ± 3 standard deviations
- X-axis: Time or sequence
- Y-axis: Metric value

✅ In-Control Process
- Points vary randomly within limits
- No clear trends or patterns

❌ Out-of-Control Signals
- Point outside UCL/LCL
- Sudden shifts or trends
- Repeated points near limits

🧪 Common Use Cases
- Marketing: Monitor ROAS, CTR, bounce rate
- Product: Funnel drop-off, error rates
- Manufacturing: Defect tracking
- Support: Call durations, wait times


__________________________________________________________________________________________________________________________________________________________________


# **1. Core Statistics & Experimentation Design**

## 📘 Index

1. [Statistical Testing](#statistical-testing)  
   1.1. [T-Tests](#t-tests)  
   1.2. [ANOVA](#anova)  
   1.3. [Chi-Square Tests](#chi-square-tests)  
   1.4. [Parametric vs Non-Parametric Alternatives](#parametric-vs-non-parametric-alternatives)  
   1.5. [Assumption Testing](#assumption-testing)


2. [Hypothesis Testing](#hypothesis-testing)  
   2.1. [Null vs. Alternative Hypotheses](#null-vs-alternative-hypotheses)  
   2.2. [Confidence Intervals & P-values](#confidence-intervals--p-values)  
   2.3. [Effect Sizes](#effect-sizes)  
   2.4. [Causality](#causality)

3. [Power Analysis & Sample Size Estimation](#power-analysis--sample-size-estimation)  
   3.1. [Minimum Detectable Effect (MDE)](#minimum-detectable-effect-mde)  
   3.2. [Sample Size Formula](#sample-size-formula)  
   3.3. [Trade-offs](#trade-offs)

4. [A/B Testing Design](#ab-testing-design)  
   4.1. [Frequentist vs Bayesian A/B Testing](#frequentist-vs-bayesian-ab-testing)  
   4.2. [Sequential Testing and FDR Correction](#sequential-testing-and-fdr-correction)  
   4.3. [Confidence vs Credible Intervals](#confidence-vs-credible-intervals)

5. [Geo Experiments & Geo Lift Analysis](#geo-experiments--geo-lift-analysis) ✅  
   5.1. [Aggregate Geo-Based A/B Tests](#aggregate-geo-based-ab-tests)  
   5.2. [Pre/Post Trends and Control Matching](#prepost-trends-and-control-matching)  
   5.3. [Applications for Brand/Media Testing](#applications-for-brandmedia-testing)

6. [Regression](#regression)  
   6.1. [Simple Linear Regression](#simple-linear-regression)  
   6.2. [Multiple Linear Regression](#multiple-linear-regression)  
   6.3. [Logistic Regression](#logistic-regression)

7. [Survival Analysis](#survival-analysis)  
   7.1. [Kaplan-Meier Curve](#kaplan-meier-curve)  
   7.2. [Log-Rank Test](#log-rank-test)  
   7.3. [Cox Regression](#cox-regression)

8. [Control Charts](#control-charts)

9. [Design of Experiments (DoE)](#design-of-experiments-doe)
      

**Further Learning**

    - Usual structure/breakdown of data collected for tests and to calculate required size
    - Understand Parametric vs. non-parametric t-tests
    - Understand test alternatives for non-equal sample size split like Welch's T-test.
    - How data should be structured to ingest and run the tests. time-series, user-level, aggregations?
    - Code for each test? manual coding? prebuilt function on statsmodels or other?
    - Build code library? Build functions packages for my own work?


10. [Libraries](#libraries)
- `scipy.stats`
- `statsmodels.stats.api` (for t-tests, ANOVA, power analysis)
- `pingouin` (for effect sizes, CI)
- `bayespy`, `PyMC`, `pymc3` (for Bayesian A/B testing)
- `GeoLift` (R package; similar analysis can be replicated in Python)
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` (for exploratory & visual analysis)

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

### ANOVA

* Extension of t-test when comparing more than two samples  
* **One-Way ANOVA**: is like an independent two sample t-test. one measurement across samples at one moment in time. It examines the effect of one independent categorical variable on a continuous variable.  
* **Two-Way ANOVA**: is like one way but tests the effect of two categorical independent variables on a continuous variable (effect on salary due to age and gender). it also evaluates the impact of the interaction of the two categorical variables.
* **Repeated Measures ANOVA**: it's like a paired t-test. Measure samples at three or more times times before and after a treatment and analyze the mean difference sample. Here samples are dependent (e.g. heart rate before workout, right after workour, 2hours after workout)
* **Mixed-Model ANOVA**: Combines repeated and between-subjects

- Requires normal distribution(if not, use Kruskal-Wallis-Test), equal variances (if not, use Welch-ANOVA), and no significant outliers. (plus for for repeated measures ANOVA, sphericity is required (Mauchly’s test)  
- F-statistic = between-group variance / within-group variance  
- If F > F-critical, reject null. Post-hoc tests are used to quantify the differences due to independent factors and interactions of multiple factors (effect size tests)

### Chi-Square Tests

* For nominal categorical variables, to see if there is a relationship between categorical variables (e.g. relationship between gender and favourite newspaper).
* Assumptions:
  - Expected frequencies per cell is greater than 5
  - account for different nominal categories without ordinal values or ranks (like categories of education (high school, Bsc, Msc, Phd). for rank copnsideration try spearman correlation, Mann-Whitney U-Test or Kruskal-Wallis-Test
* Null: no relationship; Alt: there is a relationship  
* Use chi-square statistic + degrees of freedom to determine p-value

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

## Hypothesis Testing

### Null vs. Alternative Hypotheses

_TODO: Add notes_

### Confidence Intervals & P-values

_TODO: Add notes_

### Effect Sizes

- Basically indicates how strong an observed effect is. Depending on the test you're running, the effect could be the strength of a difference or correlation.
- Cohen’s d for t-tests (0 to 1)
- r², η² for regression and ANOVA

### Causality

- Strong and significant correlation  
- Clear temporal sequence  
- Controlled experiment or theoretical reasoning

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
---

## A/B Testing Design

### Frequentist vs Bayesian A/B Testing

_TODO: Add notes_

### Sequential Testing and FDR Correction

_TODO: Add notes_

### Confidence vs Credible Intervals

_TODO: Add notes_

---

## Geo Experiments & Geo Lift Analysis ✅

### Aggregate Geo-Based A/B Tests

_TODO: Add notes_

### Pre/Post Trends and Control Matching

_TODO: Add notes_

### Applications for Brand/Media Testing

_TODO: Add notes_

---

## Regression

### Simple Linear Regression

_TODO: Add notes_

### Multiple Linear Regression

_TODO: Add notes_

### Logistic Regression

_TODO: Add notes_

---

## Survival Analysis

### Kaplan-Meier Curve

_TODO: Add notes_

### Log-Rank Test

_TODO: Add notes_

### Cox Regression

_TODO: Add notes_

---

## Control Charts

_TODO: Add notes_

---

## Design of Experiments (DoE)

_TODO: Add notes_

---

## Libraries

- `scipy.stats`  
- `statsmodels.stats.api`  
- `pingouin`  
- `bayespy`, `PyMC`, `pymc3`  
- `GeoLift`  
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly`

---

## Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here

---

## Resources

- [ ] Add articles, blogs, papers, videos, or documentation  
- [ ] [Data Tab: Full Lecture on Data Science Statistics](https://www.youtube.com/watch?v=K9teElePNkk)  
- [ ] [Statistical Power](https://www.youtube.com/watch?v=Rsc5znwR5FA&t=395s)  
- [ ] [Power Analysis and Sample Size](https://www.youtube.com/watch?v=VX_M3tIyiYk&t=246s)

