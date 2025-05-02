# **1. Core Statistics & Experimentation Design**


- **Statistical Testing**
    - T-tests (independent, paired), ANOVA
    - Chi-Square (goodness of fit & independence)
    - Confidence intervals, p-values, effect sizes
    - Power analysis & sample size estimation
    - Hypothesis testing
    - Usual structure/breakdown of data collected for tests and to calculate required size
    - Understand Parametric vs. non-parametric t-tests
    - Understand test alternatives for non-equal sample size split like Welch's T-test.
    - How data should be structured to ingest and run the tests. time-series, user-level, aggregations?
    - Code for each test? manual coding? prebuilt function on statsmodels or other?
      
- **A/B Testing Design**
    - Frequentist and Bayesian A/B testing
    - Sequential Testing, FDR correction
    - Confidence vs credible intervals
      
- **Geo Experiments & Geo Lift Analysis** ✅
    - Aggregate geo-based A/B tests
    - Pre/post trends and control-matching for regions
    - Applications for brand/media testing

### 🧰 Libraries:

- `scipy.stats`
- `statsmodels.stats.api` (for t-tests, ANOVA, power analysis)
- `pingouin` (for effect sizes, CI)
- `bayespy`, `PyMC`, `pymc3` (for Bayesian A/B testing)
- `GeoLift` (R package; similar analysis can be replicated in Python)
- `pandas`, `numpy`, `matplotlib`, `seaborn`, `plotly` (for exploratory & visual analysis)

## 📓 Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here.

## 🔗 Resources

- [ ] Add articles, blogs, papers, videos, or documentation here.

- [ ] https://www.youtube.com/watch?v=K9teElePNkk

T-Test
-     1. One sample t-test: to see if a sample mean value is significantly different from the mean reference value
-     2. Independent Samples t-test: compare significant difference between the mean value of two independent samples (two drugs, campaigns,etc.)
-     3. Paired Samples t-test: Compare means of two dependent groups where you compare the difference before and after treatment (compare mean weight of sample before and after diet)

- * t-test samples must be of normal distribution (test for normal distribution, else use non-parametric t-test like Mann–Whitney U test which tests medians rather than means)
  * In an independent two sample t-test, samples must be equal variance (test equal variance with levene's test)
  * t-test hypotheses: Null is that there is no difference, Alt is that samples are not equal/there is significant difference.
  * t-test is calculated by first getting the t-statistic (diff. in mean values / standard deviation (error)). then getting t-critical value from the t-value table by looking up the assigned p-value and sample's degrees of freedom. If our t-statistic is higher than the t-critical value, we reject the null and accept the alternative hypothesis. 

ANOVA
- Basically like T-test when you have more than two samples
- ONE WAY ANOVA is like an independent two sample t-test. one measurement across samples at one moment in time. It examines the effect of one independent categorical variable on a continuous variable.
- TWO WAY ANOVA is like one way but tests the effect of two categorical independent variables on a continuous variable (effect on salary due to age and gender). it also evaluates the impact of the interaction of the two categorical variables.
- Repeated measures ANOVA: it's like a paired t-test. Measure samples at three or more times times before and after a treatment and analyze the mean difference sample. Here samples are dependent (e.g. heart rate before workout, right after workour, 2hours after workout)
- samples data for one-way anova should be normally distributed (if not, use Kruskal-Wallis-Test) and similar variance across samples (if not, use Welch-ANOVA). for other non-normal or diff-variance anova subtypes of tests, other test alternative might apply.
- one and two way anova should have homogenity of distribution and variance. In addition for repeat measure anova, homogenity of covariance is needed (sphericity), maunchly's test is used to evaluate that. also no significant outliers.
- Mixed-Model ANOVA: analyses data within-subject factor (repeat measure), between subject-factor(one way/two way) and ther interaction between all factors.

- To calculate ANOVA: You calculate the F-statistic (variance among groups/variance within groups). Then using the assigned p-value and degrees of freedom, you extract the f-critical value. If your F-statistic is higher than F-critical, you reject the null and accept alternative. This only shows if there are statistical difference across and within samples. Post-hoc tests are used to quantify the differences due to independent factors and interactions of multiple factors (effect size tests)


Parametric and Non-parametric Tests

- Parametric Tests are used when your sample data is normally distributed. if it's not, you should then use non-parametric tests.
- Para Tests run the analysis on the raw numerical data. Non-parametric tests usually rank the numerical values, use that to create normal distributions then run the analyses. Examples of parametric tests and their non-parametric test equivalents below:

### 📊 Parametric vs Nonparametric Tests

| Test Type                          | Parametric Test                     | Nonparametric Test               | 
|-----------------------------------|-------------------------------------|----------------------------------|
| **One Sample**                    | Simple t-Test                       | Wilcoxon test for one sample     |
| **Two Dependent Samples**         | Paired Sample t-Test                | Wilcoxon Test                    |
| **Two Independent Samples**       | Unpaired Sample t-Test              | Mann–Whitney U Test              |
| **>2 Independent Samples**        | One-way (Factorial) ANOVA           | Kruskal–Wallis Test              |
| **>2 Dependent Samples**          | Repeated Measures ANOVA             | Friedman Test                    |
| **Correlation Between Variables** | Pearson Correlation                 | Spearman's Rank Correlation      |




Testing for Data Normality
1. Analytical Testing:
   - Kolmogorov-Smirnove Test (used to test other distribution types as well)
   - Shapiro-Wilk Test
   - Anderson-Darson (used to test other distribution types as well)
Null Hypothesis: Data fits normal distribution, if p less than 0.05, reject null, non-normal distribution. p greater, fail to reject and assume normal distribution.

Problems with analytical tests: p-value depends on sample size. small samples mostly yield non-representative large values. Therefore graphical tests are more frequently used.

3. Graphical Test:
- Normal histogram plotting to visually detect a bell curve
- Quantile-Quantie Plot: Normally distributed data points wold follow the disagonal line plotted as reference. non-normal would typical form an S-shape instead


Testing for Equality of Variance across data samples/groups
* Levene's Test
* Null hypothesis: Equal variance across groups
* You calculate the L-statistic(which is equal to the F-statistic) and extract the corresponding p-value. p-value less than 0.05, reject the null and variance across groups is not equal (then you cant use a t-test for example which requires homegenity of variance).
* if it was a t-test,m you can then use t test for samples with different variance

Mann-Whitney U-Test
* Non-parametric equivalent of a independent samples t-test
* Instead of comparing sample means like in t-test, MW U-test calculates rank sums and compares that.
* Null: no sig. diff in ranks sums, Alt: sig. diff.
* Calc. U-values then z-value, look that up against z-critical to determine p-value

Wilcoxon-Test
* Non-parametric equivalent of a dependent samples t-test (same sample measured before and after treatment)
* Calculate rank sums based on cross-sample differences and determine W-Statistic, then z-value, then p-value

Kruskal-Wallis-Test
* Non-parametric equivalent of a one-way ANOVA
* Calc. diff in rank sums

Friedman Test

*  Non-parametric equivalent of a repeated measures ANOVA (dependent samples)


----------------------------------------------------------

Chi-square test
* for nominal categorical variables, to see if there is a relationship between categorical variables (e.g. relationship between gender and favourite newspaper)
* Assumptions:
  - Expected frequencies per cell is greater than 5
  - account for different nominal categories without ordinal values or ranks (like categories of education (high school, Bsc, Msc, Phd). for rank copnsideration try spearman correlation, Mann-Whitney U-Test or Kruskal-Wallis-Test
  - Null: no relationship between variable, Alt: relationship
  - calculate chi-sq values, compare to critical chi-sq value and determine significance
    

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
