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
- ONE WAY ANOVA is like an independent two sample t-test. one measurement across samples at one moment in time
- TWO WAY ANOVA is like a paired t-test. Measure samples at two times before and after a treatment and analyze the mean difference sample
- samples data should be normally distributed (if not, use Kruskal-Wallis-Test) and similar variance across samples (if not, use Welch-ANOVA).
- To calculate ANOVA: You calculate the F-statistic (variance among groups/variance within groups). Then using the assigned p-value and degrees of freedom, you extract the f-critical value. If your F-statistic is higher than F-critical, you reject the null and accept alternative.

















