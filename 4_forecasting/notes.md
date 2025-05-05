# **4. Forecasting & Time-Series Analysis**

> Goal: Accurately predict key performance indicators and identify trends/seasonality in campaign or revenue data.


### 📘 Topics:

- Time-series modeling (stationary vs non-stationary)
- Forecasting techniques:
    - ARIMA, SARIMA
    - Facebook Prophet
    - LSTM (deep learning)
- Seasonality & trend decomposition
- Moving averages, exponential smoothing
- Backtesting & forecast evaluation
- Prediction Intervals (Like CI but for forecasting)

## 🎲 Monte Carlo Simulation

### 🔹 What It Is
- A **probabilistic technique** used to estimate outcomes when there is uncertainty.
- Repeatedly runs simulations using **random sampling** to generate distributions of possible results.

---

### 🔧 How It Works
1. Define the problem and model the process.
2. Identify **uncertain variables** and assign probability distributions (e.g. normal, uniform).
3. Generate **random values** for those variables (typically thousands of times).
4. Calculate the outcome for each trial.
5. Analyze the distribution of all simulated outcomes.

---

### 📦 Example Use Cases
- **Marketing**: Simulate ROI outcomes under uncertainty in campaign performance
- **Finance**: Portfolio risk, option pricing
- **Operations**: Inventory demand modeling, logistics planning
- **Data Science**: Estimate confidence intervals, p-values (bootstrap, permutation tests)

---

### 🧮 Example (Ad Campaign ROI)
Assume:
- Budget: €10,000  
- Conversion rate: normally distributed, mean = 3%, std = 0.5%  
- Revenue per conversion: €100

Run 10,000 simulations of:
1. Sample conversion rate
2. Calculate conversions = budget × sampled rate
3. Revenue = conversions × €100

Analyze:
- Mean revenue
- 5th–95th percentile (uncertainty range)
- Probability of loss

---

### 🛠️ Tools
- `numpy.random` and `scipy.stats` for distributions
- `pandas`, `matplotlib`, `seaborn` for results
- Optional: `@jit` or `numba` to speed things up

---

### ✅ When to Use It
- Too much uncertainty for deterministic formulas
- Multiple random inputs interacting in complex ways
- Need to simulate risk, not just average outcome




### 🧰 Libraries:

- `statsmodels.tsa` (ARIMA, seasonal decomposition, ETS)
- `prophet` (by Meta; clean API for quick forecasting)
- `pmdarima` (auto ARIMA modeling)
- `tensorflow` / `keras` (LSTM models)
- `sktime` (unified interface for time-series modeling and backtesting)
- `plotly`, `matplotlib`, `seaborn` (for visual inspection)
  
## 📓 Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here.

## 🔗 Resources

- [ ] Add articles, blogs, papers, videos, or documentation here.
