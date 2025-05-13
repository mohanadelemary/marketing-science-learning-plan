# **3. Marketing Attribution & MMM**

> Goal: Apply statistical and causal techniques to marketing attribution and media impact measurement.


### 📘 Topics:

- **Attribution Models**
    - Multi-Touch Attribution (MTA)
    - Shapley Value Attribution
    - Markov Chain Attribution
- **Marketing Mix Modeling (MMM)**
    - Baseline estimation, adstock, saturation
    - Revenue decomposition by channel
    - Model calibration using holdout or geo testing
    - Bayesian MMM

### 🧰 Libraries:

- `Facebook Robyn` (R, but used in industry for MMM — alternative logic can be replicated in Python)
- `causalimpact` (intervention-based MMM)
- `bayespy`, `PyMC` (Bayesian MMM)
- `Shap` (Shapley values for explainability)
- `markovify`, `networkx` (custom Markov chain attribution models)
- `lifetimes` (used sometimes in LTV estimation alongside attribution)
- `pandas`, `numpy`, `matplotlib`, `seaborn`
  
## 📓 Notes & Summaries

- [ ] Add theoretical explanations, formulas, and insights here.

## 🔗 Resources

- [ ] Add articles, blogs, papers, videos, or documentation here.


## 4. Marketing Attribution & MMM

---

### 🎯 Goal

Apply **statistical** and **causal inference techniques** to:
- Quantify the impact of each marketing channel
- Assign credit across touchpoints
- Estimate channel ROI and forecast budget outcomes
- Separate base demand from media-driven effects

---

### 📘 Topics

#### ✅ Attribution Models (Rule-Based and Probabilistic)
- **Last Click / First Click**  
  Simple but biased — ignores multi-channel interaction
- **Linear**  
  Equal credit across all touchpoints
- **Time Decay**  
  Higher credit to recent touches
- **Position-Based**  
  Custom weights: first + last click get more

#### ✅ Multi-Touch Attribution (MTA)
- Model-based methods that assign value across the customer journey
- Use data-driven techniques (logistic regression, tree models) to predict conversion likelihood from sequences
- Can integrate with Shapley or Markov to improve interpretability

#### ✅ Shapley Value Attribution
- Based on cooperative game theory
- Calculates **marginal contribution** of each channel across all possible combinations
- Often used in combination with machine learning models for explainability

#### ✅ Markov Chain Attribution
- Models customer journey as a **Markov process**
- Calculates removal effect: how conversion probability drops when a channel is removed
- Good for capturing **path dependencies** and **drop-off behavior**

#### ✅ Marketing Mix Modeling (MMM)
- Statistical model (often linear or log-log) that regresses **sales** or **revenue** on media spend + control variables
- Key components:
  - **Baseline estimation**: Isolates organic demand
  - **Adstock / carryover**: Media impact persists over time
  - **Saturation**: Diminishing returns at higher spend
- Useful for **long-term**, **channel-level** budget planning

#### ✅ Revenue Decomposition by Channel
- Use MMM coefficients or Shapley values to split total revenue into media-contributed vs. baseline

#### ✅ Model Calibration
- Validate MMM or MTA models using:
  - **Holdout campaigns**
  - **Geo testing** (e.g. turn off spend in certain regions)

#### ✅ Bayesian MMM
- Enhances traditional MMM with:
  - **Credible intervals**
  - Prior knowledge (e.g. plausible lift ranges)
  - Hierarchical modeling across markets or products

---

### 🧰 Libraries

#### ✅ Attribution & Path Modeling
- `markovify`, `networkx`  
  Build Markov chain attribution logic and visualize path flows
- `Shap`  
  Compute Shapley values from any machine learning model

#### ✅ MMM & Media Impact Estimation
- `Facebook Robyn` (R)  
  Industry-standard for MMM; open-source with automated adstock + saturation tuning
- `causalimpact`  
  Useful for campaign-level lift estimation (Bayesian structural time series)
- `PyMC`, `pymc3`, `bayespy`  
  For Bayesian MMM with priors and uncertainty

#### ✅ Supporting Tools
- `lifetimes`  
  LTV modeling — often used alongside attribution to model downstream value
- `pandas`, `numpy`, `matplotlib`, `seaborn`  
  Data wrangling, summary stats, visualizations

---

### 🧠 Tip

Use **attribution models for tactical insights** (e.g., channel-level ROAS)  
Use **MMM for strategic budgeting** across channels, including offline spend

