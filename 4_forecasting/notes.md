## 4. Forecasting & Time-Series Analysis

Goal: Accurately predict key performance indicators and identify trends, seasonality, and uncertainty in campaign or revenue data.


### Index

- [4.1 Time-Series Fundamentals](#41-time-series-fundamentals)  
- [4.2 Time-Series Decomposition](#42-time-series-decomposition)  
- [4.3 Classical Forecasting Models](#43-classical-forecasting-models)  
- [4.4 Automated Forecasting](#44-automated-forecasting)  
- [4.5 Deep Learning for Time-Series](#45-deep-learning-for-time-series)  
- [4.6 Forecast Evaluation & Backtesting](#46-forecast-evaluation--backtesting)  
- [4.7 Prediction Intervals](#47-prediction-intervals)  
- [4.8 Monte Carlo Simulation for Forecasting](#48-monte-carlo-simulation-for-forecasting)
- [4.9 When to Use What?](#49-when-to-use-what?)  
- [4.10 Tools & Libraries](#410-tools--libraries)  
- [4.11 AI Tools for Forecasting, Anomaly Detection and Computer Vision Analysis](#411-ai-tools-for-forecasting-anomaly-detection-and-computer-vision-analysis)   
---

### 4.1 Time-Series Fundamentals


#### What Makes Time-Series Data Unique?

- Observations are **ordered in time**, and order **matters**
- Values are often **autocorrelated** — past values influence future values
- Requires **time-aware methods** that account for:
  - Trends
  - Seasonality
  - Lags
  - Volatility over time

Unlike typical regression data, you **cannot randomly shuffle rows** without breaking the time-dependent structure.

---

#### Stationarity vs. Non-Stationarity

- **Stationary**: statistical properties (mean, variance, autocorrelation) are **constant over time**
  - Needed for many models (e.g., ARIMA)
  - Easier to forecast
- **Non-Stationary**: properties change over time
  - Trend or seasonality may dominate
  - Must be transformed before modeling

📌 Why it matters:
- Most time-series models assume stationarity
- Stationarity improves **forecast stability** and **model reliability**
- Raw data like revenue for example wouldn't follow stationarity if it's going through growth, therefore requires transformation first.

**How to check for stationarity**:
- Visual inspection: trend? changing variance?
- **Augmented Dickey-Fuller test (ADF)** → low p-value (< 0.05) suggests stationarity

---

#### 🔧 Making Data Stationary

1. **Differencing**: subtract previous value to remove trend  
   \[
   y'_t = y_t - y_{t-1}
   \]
   
    | Time | Revenue | Difference |
    |------|---------|------------|
    | t1   | 100     | —          |
    | t2   | 120     | 20         |
    | t3   | 140     | 20         |
    | t4   | 160     | 20         |

3. **Log transformation**: stabilizes variance  
   \[
   y'_t = \log(y_t)
   \]

    | Time | Revenue | Log(y) |
    |------|---------|--------|
    | t1   | 100     | 4.61   |
    | t2   | 200     | 5.30   |
    | t3   | 400     | 5.99   |
    | t4   | 800     | 6.68   |
   
   Variance is compressed as values grow.
   
5. **Detrending**: subtract fitted trend component

    \[
    y'_t = y_t - \hat{y}_t^{(trend)}
    \]

    | Time | Revenue | Fitted Trend | Detrended |
    |------|---------|--------------|-----------|
    | t1   | 100     | 95           | +5        |
    | t2   | 110     | 105          | +5        |
    | t3   | 120     | 115          | +5        |
    | t4   | 130     | 125          | +5        |


6. **Seasonal differencing**: remove repeating patterns
   
    Removes **repeating seasonal patterns** (e.g., yearly trend in monthly data):
    
    \[
    y'_t = y_t - y_{t-s}
    \]
    
    ✅ Example: \( s = 12 \) → for **monthly data with yearly seasonality**
    
    | Month | Revenue | Seasonal Difference (t - t-12) |
    |--------|---------|-------------------------------|
    | Jan Y1 | 120     | —                             |
    | Feb Y1 | 130     | —                             |
    | ...    | ...     | —                             |
    | Dec Y1 | 160     | —                             |
    | Jan Y2 | 180     | 180 - 120 = 60                |
    | Feb Y2 | 190     | 190 - 130 = 60                |
    
    📌 This transformation removes **recurring patterns** across the same period each year.

---

#### How to Choose the Right Time-Series Transformation

**Step 1: Plot the Data**
    
- Is the series **trending up/down**? → Likely **non-stationary trend**
- Is the **variance increasing over time**? → Consider log or Box-Cox
- Are there **repeating seasonal patterns**? → Seasonal differencing needed
- Does it look “bumpy” but stable? → It might already be stationary

**Step 2: Visual & Statistical Checks**

| Check                        | Tool / Test                     | Interpretation                     |
|------------------------------|----------------------------------|-------------------------------------|
| Trend                        | Line plot                        | Sloped pattern = trend              |
| Seasonality                  | Seasonal plot, autocorrelation  | Peaks/lags at fixed intervals       |
| Non-constant variance        | Rolling std or residual plot     | Increasing spread = heteroscedasticity |
| Stationarity (overall)       | ADF Test (Augmented Dickey-Fuller) | p < 0.05 → likely stationary        |

**Transformation Cheatsheet** 

| Problem                      | Use This Transformation            | Example Model After |
|-----------------------------|-------------------------------------|---------------------|
| **Trend**                   | First-order differencing            | ARIMA               |
| **Seasonality**             | Seasonal differencing (lag = season length) | SARIMA              |
| **Increasing variance**     | Log or Box-Cox transformation       | ARIMA / ETS         |
| **Linear trend**            | Detrending (subtract regression line) | AR model            |
| **Both trend & variance**   | Log → differencing                  | ARIMA               |


**Practical Strategy (Robust)**

1. Start with **plotting the raw data**
2. Apply **log transformation** if variance grows with level
3. Check again — if still trending, apply **first-order differencing**
4. If there's seasonality (e.g. monthly pattern), apply **seasonal differencing**
5. Test final series with **ADF test** to confirm stationarity

**Summary**

- You often **stack transformations**: log → diff → seasonal diff
- Always **test and visualize** after each step
- Your model (ARIMA, SARIMA) choice depends on which non-stationarities remain

---

#### 📈 Trend, Seasonality & Noise

| Component     | Description                                        | How to Detect            |
|---------------|----------------------------------------------------|---------------------------|
| **Trend**     | Long-term increase/decrease in mean                | Line slopes upward/downward |
| **Seasonality** | Repeating patterns at fixed intervals (weekly, yearly) | Peaks/valleys in consistent intervals |
| **Noise**     | Random, irregular variation                        | Unexplained by trend or seasonality |

🧪 Visual tools:
- Plot time series
- Use **STL decomposition** to isolate components (covered in 4.2)


#### ✅ Summary

| Concept         | Role in Forecasting                      |
|------------------|------------------------------------------|
| Stationarity     | Required for many models (e.g. ARIMA)   |
| Differencing     | Removes trend or seasonal structure     |
| Seasonality      | Must be modeled explicitly (e.g. SARIMA)|
| Trend            | Can distort forecasts if not handled    |
| Noise            | Limits forecasting accuracy             |


---

### 4.2 Time-Series Decomposition

#### 🧠 What Is Time-Series Decomposition?

Decomposition splits a time-series into **three main components**:

\[
\text{Time Series} = \text{Trend} + \text{Seasonality} + \text{Residual (Noise)}
\]

This helps you **understand**, **visualize**, and sometimes **model** different dynamics separately.

---

#### ➕ Additive vs. ✖️ Multiplicative Decomposition

| Type           | Formula                                     | When to Use                                     |
|----------------|---------------------------------------------|-------------------------------------------------|
| **Additive**   | \( y_t = T_t + S_t + e_t \)                 | Components are independent and stable over time |
| **Multiplicative** | \( y_t = T_t \times S_t \times e_t \)   | Seasonal fluctuations grow/shrink with the level of the series |

📌 Rule of thumb:  
- Use **additive** if the **amplitude of seasonality is constant**
- Use **multiplicative** if **seasonality increases with trend**

---

#### 🔍 STL Decomposition (Seasonal-Trend decomposition using Loess)

- STL = **flexible, robust method** for **additive decomposition**
- Handles:
  - **Nonlinear trends**
  - **Irregular seasonality**
  - **Outliers** better than classical decomposition
- Uses **Loess smoothing** (locally weighted regression)

- Note: STL works strictly on Additive Time-Series Models. If your data is multiplicative in nature, applying log transformation switches it to additive, then you can apply STL.


#### 🛠️ Example Output of STL

| Component      | Description                                 |
|----------------|---------------------------------------------|
| **Trend**      | Underlying direction of the series          |
| **Seasonal**   | Repeating pattern (daily, weekly, yearly)   |
| **Residual**   | What's left (random noise or unexplained)   |

🧪 Visual: STL produces a 4-panel plot:
- Observed → Trend → Seasonality → Remainder


#### 🔍 Why/When Use Decomposition?

| Use Case                           | How Decomposition Helps                   |
| ---------------------------------- | ----------------------------------------- |
| **Diagnostics**                    | Understand what drives non-stationarity   |
| **Feature Engineering**            | Use trend/seasonality as features in ML   |
| **Anomaly Detection**              | Spot outliers in the residuals            |
| **Modeling Strategy**              | Fit ARIMA on residual (de-trended series) |
| **Visualization for Stakeholders** | Communicate trend vs. seasonality clearly |

#### ✅ Summary

1. Use decomposition to break down the time series before modeling
2. Choose additive or multiplicative based on amplitude behavior
3. STL is robust, interpretable, and supports irregular seasonalities
4. Decomposition ≠ forecasting → it’s for understanding and preparation


---

### 4.3 Classical Forecasting Models


Classical models are built to capture **trend**, **seasonality**, and **autocorrelation** in time series. They're often interpretable, fast, and work well on low-to-medium complexity datasets.

#### 🔁 AR, MA, ARMA, ARIMA – Core Definitions

| Model    | Formula                             | Captures                         | Assumes Stationarity? |
|----------|-------------------------------------|----------------------------------|------------------------|
| **AR(p)** | y_t = φ₁·y_{t-1} + ... + φₚ·y_{t-p} + ε_t   | Autoregression: uses past values | ✅ Yes |
| **MA(q)** | y_t = ε_t + θ₁·ε_{t-1} + ... + θ_q·ε_{t-q} | Moving Average: uses past errors | ✅ Yes |
| **ARMA(p, q)** | Combines AR and MA             | Short-term memory & noise        | ✅ Yes |
| **ARIMA(p, d, q)** | Includes differencing to remove trend | Non-stationary + autoregressive + error memory | ❌ No → makes it stationary through differencing |

📌 ARIMA is the go-to for **trend-based forecasting** after making the series stationary.

---

#### ❄️ SARIMA (Seasonal ARIMA)

SARIMA = ARIMA + seasonal components

Structure:  
**SARIMA(p, d, q) (P, D, Q, s)**

- (p, d, q): non-seasonal ARIMA terms
- (P, D, Q): seasonal counterparts
- s = season length (e.g., 12 for monthly series with yearly cycles)

Example:  
**SARIMA(1,1,1)(1,1,0,12)** → a model with yearly seasonality on monthly data

| Component | Description                                  |
|-----------|----------------------------------------------|
| **D**     | Seasonal differencing                        |
| **P**     | Seasonal autoregression                      |
| **Q**     | Seasonal moving average                      |
| **s**     | Seasonality length (e.g. s=7 for weekly cycle)|

🧪 Example: SARIMA(1,1,1)(1,1,0,12) = monthly sales data with yearly seasonality

---

#### 📉 Exponential Smoothing & Holt-Winters

Unlike ARIMA, exponential smoothing directly **models levels, trends, and seasonality** using weighted averages.

| Model                 | Handles                  | Notes                            |
|----------------------|--------------------------|----------------------------------|
| **Simple Exponential Smoothing** | Flat series (no trend/seasonality) | Short-term, memory-based        |
| **Holt's Linear Trend** | Trend only               | Adds slope adjustment            |
| **Holt-Winters (Triple)** | Trend + Seasonality     | Additive or multiplicative components |

📌 Forecasts are built by updating components at each time step:
\[
\text{Forecast} = \text{Level} + \text{Trend} + \text{Seasonality}
\]


| Use Case                              | Benefit                                    |
|---------------------------------------|--------------------------------------------|
| Forecast daily or weekly conversions  | Simple, quick estimate for planning        |
| React to short-term trend shifts      | More responsive than a rolling average     |
| Campaign pacing or budget throttling  | Helps adjust spend if volume dips/rises    |
| Low-data environments                 | Doesn’t need much historical data          |

---

#### ⚖️ ARIMA vs. Exponential Smoothing

| Feature               | ARIMA                              | Exponential Smoothing          |
|------------------------|-------------------------------------|---------------------------------|
| Requires stationarity  | ✅ Yes                             | ❌ No                           |
| Models trend directly  | ❌ No (needs differencing)         | ✅ Yes                          |
| Forecasts based on     | Past values + past errors          | Smoothed levels/trends         |
| Better for             | Statistical series, longer memory  | Business data with cycles      |

---

#### ✅ Summary

- Use **ARIMA** for series with autocorrelation and trend
- Use **SARIMA** when seasonality is present
- Use **Exponential Smoothing** for interpretable, short-term business forecasting
- Choose models based on **stationarity, seasonality**, and **forecast horizon**

---

 ### 4.4 Automated Forecasting

Automated forecasting tools simplify model selection, fitting, and tuning. They reduce the need to manually test ARIMA parameters or hand-code trend/seasonality logic, making them ideal for business forecasting workflows.

---

#### 📈 Facebook Prophet

> Built by Meta for business time series forecasting with **trend, seasonality, and holiday effects**.

**Key Features:**
- Models **trend**, **weekly/yearly seasonality**, and **holiday effects**
- Handles **missing data**, **outliers**, **non-daily intervals**
- Provides **prediction intervals**
- Uses additive or multiplicative model:
  `y(t) = trend(t) + seasonality(t) + holiday(t) + error(t)`

**Use Cases:**
- Daily or weekly revenue
- Search ad conversions
- Season-sensitive forecasting (e.g. Black Friday)

---

#### 🔄 pmdarima (Auto-ARIMA)

> Automatically finds the best ARIMA/SARIMA model using AIC/BIC.

**Key Features:**  
- Grid search over ARIMA parameters (p, d, q)
- Automatically applies differencing (d) if needed
- Seasonality supported via seasonal=True
- Works well for univariate, structured time series

**Use Cases:**
- Forecasting search spend, impressions, conversions
- When you don’t want to manually test differencing/order

---

#### 🔁 sktime & statsforecast (Advanced Libraries)

- **sktime**
    - Scikit-learn-style interface for time series
    - Use Case: Unified tools for regression + forecasting
    - Easy backtesting and cross-validation
    - Support for classical and ML-based forecasters
    - Compatible with pandas time indexes

      
- **statsforecast**
    - Fast forecasting with ARIMA, ETS, Prophet-style models
    - Use Case: High-performance forecasting in production
    - Built for scale (millions of time series)
    - Models: ARIMA, AutoETS, Prophet-style growth
    - Uses numba for speed; works well with distributed workflows


### 🧠 When to Use What

| Tool            | Best For                                                    |
|------------------|-------------------------------------------------------------|
| **Prophet**       | Business data with trend, seasonality, holidays             |
| **pmdarima**      | Structured series with autocorrelation + seasonality        |
| **sktime**        | Experiments, hybrid ML models, pipeline integration         |
| **statsforecast** | High-volume, production-scale forecasting                   |


**✅ Summary**

- Prophet is great for business forecasting with known events
- Auto-ARIMA removes the manual pain of order selection
- sktime offers flexibility for cross-validation + ML integration
- statsforecast is fast and scalable for large-volume jobs

---

#### 📊 Using External Regressors in Prophet (e.g. Ad Spend)

- Prophet allows adding **external variables** (e.g. ad spend, discounts, competitor signals) as regressors.
- You must call `.add_regressor('column_name')` during model setup.
- These variables must be:
  - Numeric and time-aligned with the date column (`ds`)
  - Supplied with **future values** during forecasting
- Useful for modeling the **impact of marketing actions** on KPIs like conversions or revenue.

**✅ Example Use Cases:**  
- Google Search Ads spend → conversion forecasts
- Discounts → promo sales spikes
- Competitor activity → brand traffic dips

📌 Prophet doesn't forecast regressors — **you provide their future values manually**.

---

#### 🧠 Do Other Forecasting Packages Support External Regressors?

| Tool            | Supports Regressors? | How It Works                                      |
|------------------|----------------------|----------------------------------------------------|
| **Prophet**       | ✅ Yes               | Add manually via `.add_regressor()` and provide future values |
| **sktime**        | ✅ Yes (via pipelines) | Combine forecasters with exogenous features using regression models |
| **statsforecast** | ✅ Limited           | Some models support exogenous inputs (e.g. ARIMA with X) |
| **pmdarima**      | ✅ Yes               | Use `exogenous` argument (`exog`) in fit and predict methods |
| **AutoTS (Python)** | ✅ Yes             | Accepts regressors in the modeling pipeline        |

### ✅ General Rules

- Regressors = external numeric variables aligned with timestamps
- You **must supply future values** at prediction time (no automatic regressor forecasting)
- Often used for: **ad spend, discounts, weather, traffic, competitor trends**

---

### 4.5 Deep Learning for Time-Series

Deep learning models, especially LSTMs, are powerful for **modeling complex, nonlinear patterns** in time series — especially when classical models fall short.

---

#### 🧠 LSTM Architecture Basics

- **LSTM (Long Short-Term Memory)** is a type of RNN designed to capture **long-range temporal dependencies**
- It maintains a **memory cell** that can retain relevant information over time
- LSTMs use **gates** (input, forget, output) to control what to keep, discard, or output at each step

📌 Compared to vanilla RNNs:
- LSTMs are **less prone to vanishing gradients**
- Better at modeling **longer sequences and multivariate inputs**

---

#### ⚡ When LSTMs Outperform Classical Models

| Scenario                                      | Why LSTM Wins                                   |
|-----------------------------------------------|-------------------------------------------------|
| Highly nonlinear patterns                     | Captures complex temporal dependencies          |
| Multivariate inputs (e.g. spend, clicks, CPC) | Learns interactions across features and time    |
| Noisy or irregular data                       | More robust than rigid statistical assumptions  |
| Very large datasets                           | Scales better than ARIMA-like models            |

But: they require **more data, tuning, and computation**, and are **less interpretable** than models like ARIMA or Prophet.

---

#### 🛠️ Keras / TensorFlow Implementation Highlights

- Use `LSTM` layers to process sequences
- Input shape: `(samples, time_steps, features)`
- Can stack LSTMs or combine with Dense layers for output
- Requires normalization, sequence batching, and careful validation

📌 Common use cases:
- Predicting future ad conversions using prior days + channel inputs
- Modeling delayed effects from search ads spend
- Learning sequence-to-one (e.g. forecast next day) or sequence-to-sequence outputs

---
#### 🧠 Use Case: Modeling Delayed Effects from Search Ads Spend with LSTM

**📈 The Problem:** In performance marketing, **ad spend today** doesn’t always result in **conversions today**.

- **Lag effects**: conversions happen 1–3+ days later
- **Spillover**: awareness builds over time
- **Attribution windows**: events attributed later

**🔁 How LSTM Helps**: LSTM can **learn lagged dependencies** automatically by:

- Observing patterns across sequences (e.g., spend → conversions days later)
- Capturing cumulative effects over time (not just day-by-day spikes)

✅ Input: sequences of past daily features (e.g., last 7–30 days)
- Search Spend, Impressions, CPC, CTR, etc.

✅ Output: conversions or revenue at time `t`

**📦 Example Input Structure (X) to LSTM**

| Day (t-n to t) | Search Spend | CPC | Clicks |
|----------------|--------------|-----|--------|
| t-6            | 1200         | 1.2 | 1000   |
| t-5            | 1300         | 1.1 | 1100   |
| ...            | ...          | ... | ...    |
| t-1            | 1400         | 1.0 | 1150   |

→ **Predict conversions at time t**

---

#### 🛠️ Transfer Learning vs. Build From Scratch

| Option              | When to Use                                     | Pros                        | Cons                       |
|---------------------|--------------------------------------------------|-----------------------------|----------------------------|
| **Build from Scratch** | You have **enough campaign-specific data**     | Fully tailored to your data | Needs more data and time   |
| **Transfer Learning** | You want to **leverage pre-trained model**     | Faster, uses learned weights| Might not generalize well  |

> Most marketing teams **build from scratch** with historical data per account or product category, especially when input features are domain-specific (e.g., CPC, match type).

You could also train on one account, then **fine-tune** on another with fewer data points.

**✅ Summary**

- LSTMs are powerful for **high-dimensional**, **nonlinear**, **long-memory** time series
- Best used when classical models are too rigid
- Needs more data and effort, but can capture complex ad performance dynamics

---

### 4.6 Forecast Evaluation & Backtesting

Evaluating forecast performance is critical to avoid overfitting and assess real-world accuracy. Time-series data requires **time-aware validation techniques** — traditional random splits don’t apply.

---

#### 🔁 Holdout vs. Rolling Forecast Origin

| Method                     | Description                                                      | Use Case                                  |
|----------------------------|------------------------------------------------------------------|-------------------------------------------|
| **Holdout Split**          | Train on past → test on future (fixed window)                   | Simple benchmarking for single horizon    |
| **Rolling Forecast Origin** | Incrementally shift training window forward (walk-forward)      | Evaluates **model consistency** over time |
| **Expanding Window**       | Add more past data with each iteration                          | Reflects learning as more data accumulates|

📌 Rolling evaluation better simulates real deployment:  
"Re-train every week, re-forecast next period"

---

#### 🔀 Cross-Validation for Time Series

Classic k-fold CV doesn’t apply to time series because it breaks temporal order.

Instead, use:
- **TimeSeriesSplit** (from scikit-learn or sktime)
- **Backtesting utilities** (e.g., `cross_val_score()` in sktime, Prophet CV wrapper)

These simulate:
- Training on t₁ → tₙ
- Testing on tₙ₊₁ → tₙ₊ₕ

Repeat with shifted cutoffs.

---

#### 📏 Forecast Accuracy Metrics

| Metric      | Formula                                 | Description & Notes                              |
|-------------|------------------------------------------|--------------------------------------------------|
| **MAE**     | mean(|y - ŷ|)                            | Average absolute error, easy to interpret        |
| **RMSE**    | sqrt(mean((y - ŷ)²))                     | Penalizes larger errors more heavily             |
| **MAPE**    | mean(|(y - ŷ) / y|) × 100%               | % error; not defined when y = 0                  |
| **SMAPE**   | mean(2·|y - ŷ| / (|y| + |ŷ|)) × 100%     | Safer MAPE alternative with symmetric scaling    |
| **Coverage Rate** | % of true values within prediction intervals | Measures **uncertainty calibration**             |

---

### ✅ Summary

- Use **rolling or expanding window** for realistic validation
- Evaluate using multiple metrics — MAPE for % scale, RMSE for penalty
- Include **coverage rate** if your model outputs intervals
- Time-aware cross-validation is essential for production readiness

---

### 4.7 Prediction Intervals

Forecasts aren’t just about predicting a **point value** — you should also estimate the **uncertainty** around that prediction. This is where **prediction intervals** come in.

---

#### 📏 Confidence Interval vs. Prediction Interval

| Concept               | What It Covers                                | Use Case                        |
|------------------------|-----------------------------------------------|----------------------------------|
| **Confidence Interval** | Uncertainty around the **mean forecast**        | “We’re 95% confident the *average* conversion is 200 ± 20” |
| **Prediction Interval** | Range for a **single future observation**      | “There’s a 95% chance tomorrow’s conversion is between 160–240” |

📌 In time series, we care more about **prediction intervals** because we’re predicting **specific future values**, not just model averages.

---

#### 🧠 How to Calculate Prediction Intervals

Depends on the model type:

| Model             | Method for Intervals                       |
|--------------------|--------------------------------------------|
| **Prophet**         | Automatically estimates using quantiles (80%, 95%) |
| **ARIMA/SARIMA**    | Based on standard error of forecast (± Z·σ) |
| **Bootstrapped Models** | Refit on resampled data → take percentiles |
| **Machine Learning** | Use quantile regression or conformal prediction |

---

#### 🎲 Bootstrapping + Quantile Estimation

Bootstrapping = simulating multiple forecasts using:
- Resampling the residuals
- Re-fitting the model multiple times
- Collecting outcomes → estimate uncertainty via percentiles

| Percentile     | Interpretation                              |
|----------------|----------------------------------------------|
| 10th & 90th    | 80% prediction interval                      |
| 2.5th & 97.5th | 95% prediction interval                      |

This works even for **non-parametric models** like XGBoost, Random Forests, or LSTMs.

---

#### ✅ Summary

- **Prediction intervals** reflect uncertainty in future values, not just model confidence
- Use intervals to communicate **risk** in forecasts (e.g. min/max revenue)
- Can be calculated via:
  - **Built-in model logic** (Prophet, ARIMA)
  - **Bootstrapping or quantile models**
- Always report intervals alongside point forecasts in dashboards or reports

---

### 4.8 Monte Carlo Simulation for Forecasting

Monte Carlo Simulation is a **probabilistic technique** used to simulate a range of possible outcomes when there’s **uncertainty in inputs**. It’s especially useful in marketing for forecasting **risk, ROI, and budget outcomes**.

---

#### 🎲 What It Is & Why It’s Useful

- Instead of one fixed forecast, it produces **thousands of randomized outcomes**
- Helps answer: “What’s the best/worst/most likely result?”
- Reflects **real-world uncertainty** in variables like conversion rate, CPC, spend

---

#### ⚙️ Setting Up Probabilistic Inputs

Define **uncertain inputs as probability distributions**:

| Input               | Example Distribution                |
|----------------------|-------------------------------------|
| Conversion Rate      | Normal (mean = 0.03, std = 0.005)   |
| Revenue per Order    | Uniform (min = €80, max = €120)     |
| Daily Spend          | Triangular or log-normal            |

Then simulate:
- Draw random values from each distribution
- Compute outcomes (e.g. revenue = conversions × order value)
- Repeat 1,000–10,000 times

---

#### 📊 Simulating Forecast Distributions

Each simulation gives a possible outcome. After many runs:

- Get **mean forecast**
- Compute **prediction intervals** (e.g. 5th–95th percentile)
- Assess **probability of loss** or **exceeding target**

---

#### 📦 Applications in Marketing Analytics

| Scenario                         | Monte Carlo Use Case                            |
|----------------------------------|-------------------------------------------------|
| Forecast ROI                     | Account for uncertainty in spend, CPA, AOV      |
| Budget planning                  | Simulate different spend scenarios and outcomes |
| Campaign risk estimation         | Estimate probability of underperformance        |
| Performance guarantees           | Quantify risk in client-facing commitments      |

---

### 🎯 Monte Carlo vs. Deterministic Forecasting

---

| Feature                  | Deterministic Forecasting                      | Monte Carlo Simulation                            |
|--------------------------|------------------------------------------------|----------------------------------------------------|
| **Type of Output**       | Single value (point forecast)                 | Distribution of possible outcomes                 |
| **Input Type**           | Fixed, known inputs                           | Random variables with probability distributions   |
| **Uncertainty Handling** | Ignores uncertainty (or handles it crudely)   | Explicitly models uncertainty                     |
| **Forecast**             | “We expect €20,000 in revenue next month”     | “Revenue will likely fall between €18K–€25K (90%)” |
| **Examples**             | ARIMA, Prophet (point only), Exponential Smoothing | Monte Carlo Simulation, Bayesian models         |

---

### 🧠 Key Difference

- **Deterministic** = one fixed outcome based on one set of assumptions
- **Monte Carlo** = thousands of simulations using **randomized inputs**, producing a **range** of likely outcomes

---

### ✅ When to Use Monte Carlo

| Use Case                             | Why Monte Carlo Helps                     |
|--------------------------------------|--------------------------------------------|
| Budgeting & planning under uncertainty | Accounts for variable ad performance       |
| Campaign ROI simulations             | Models best/worst case scenarios           |
| Revenue forecasts with input ranges  | Captures volatility in conversion rate, spend, CPC |

- Deterministic forecasting = useful for baselines
- Monte Carlo = better for **risk-aware**, **realistic**, **uncertainty-informed** decisions

---

#### ✅ Summary

- Monte Carlo simulates **many possible futures**, not just averages
- Useful when multiple inputs are **uncertain** and interact in nonlinear ways
- Helps make **risk-aware** decisions for spend, revenue, and ROI forecasts

---

### 4.9 When to Use What?

| Scenario                                | Recommended Model(s)                       | Why It Works                                     |
|-----------------------------------------|---------------------------------------------|--------------------------------------------------|
| **Short time series** (e.g. < 2 years)  | Exponential Smoothing, Prophet              | Works with limited data, handles trends well     |
| **Strong seasonality (e.g. weekly, yearly)** | SARIMA, Prophet, Holt-Winters          | Built-in seasonality handling                    |
| **High autocorrelation, no seasonality**| ARIMA, Auto-ARIMA                           | Captures trends and lag structure                |
| **Irregular or missing time intervals** | Prophet                                     | Handles missing dates natively                  |
| **Many time series (at scale)**         | statsforecast, sktime pipelines             | Built for high-volume, production environments   |
| **Need for uncertainty estimates**      | Prophet, Bayesian models, Monte Carlo       | Provides intervals and probabilistic output      |
| **Highly nonlinear patterns or lags**   | LSTM, RNNs                                  | Learns complex dependencies across time          |
| **You need full automation**           | Auto-ARIMA, Prophet, statsforecast          | Minimal tuning required                          |
| **Causal/external factors involved**    | Prophet w/ regressors, sktime + exog        | Incorporates marketing variables (e.g. ad spend) |


- Use **classical models** (ARIMA, ETS) for interpretable, structured data
- Use **automated tools** (Prophet, pmdarima) for fast deployment
- Use **LSTM/NNs** for large, nonlinear, multivariate datasets
- Always match the model to your **data structure and business needs**

> **Footnote:** While Prophet is excellent for forecasting with seasonality and external regressors, models like **XGBoost or other gradient-boosted regressors** offer additional flexibility:
> - **Custom Thresholds**: They can directly incorporate business rules or thresholds (like minimum incremental ROAS) into the modeling process, ensuring predictions align with strategic business goals.
> - **Optimization**: They allow for fine-tuning and optimization based on custom performance metrics, making them powerful for scenarios where meeting specific thresholds is crucial.
> - **Non-linear Relationships**: They excel at capturing complex, non-linear relationships between variables, which can provide more accurate and actionable insights for marketing spend optimization.

---
### 4.10 Tools & Libraries
- `statsmodels.tsa`: ARIMA, decomposition, ETS
- `prophet`: Easy-to-use forecasting from Meta
- `pmdarima`: Auto ARIMA modeling
- `sktime`: Unified interface for classical and ML forecasting
- `tensorflow / keras`: LSTM, deep learning models
- `numpy`, `scipy.stats`: For Monte Carlo and uncertainty simulation
- `plotly`, `matplotlib`, `seaborn`: For visualizing forecasts

---

### 4.11 AI Tools for Forecasting, Anomaly Detection and Computer Vision Analysis

**Ad Performance & Creative Optimization**
- **Anomaly Detection**
    - Time-series outlier detection, Change point detection in marketing data (`PyOD`, `Prophet`, `TensorFlow Anomaly Detection`)
- **Audience Segmentation & Personalization**
    - Clustering (K-Means, DBSCAN, Gaussian Mixture Models, Hierarchical Clustering), Look-Alike Modeling (`scikit-learn`, `HDBSCAN`, `LightFM`, `Surprise`)
- **NLP for Sentiment Analysis**
    - Analyzing customer feedback & engagement (`spaCy`, `Transformers`)
- **Computer Vision for Ad Performance**
    - Analyzing ad creatives (`OpenCV`, `DeepCTR`)

---

