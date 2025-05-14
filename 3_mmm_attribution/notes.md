## 3. Marketing Attribution & MMM

1. [Attribution vs. MMM – Quick Comparison](#1-attribution-vs-mmm--quick-comparison)  
2. [Attribution Modeling](#2-attribution-modeling)  
   2.1. [What Is Attribution?](#21-what-is-attribution)  
   2.2. [Types of Attribution Models](#22-types-of-attribution-models)  
   2.3. [Data Structure for Attribution](#23-data-structure-for-attribution)  
   2.4. [How to Build Attribution Models](#24-how-to-build-attribution-models)  
   2.5. [Attribution Libraries](#25-attribution-libraries)  
3. [Marketing Mix Modeling (MMM)](#3-marketing-mix-modeling-mmm)  
   3.1. [What Is MMM?](#31-what-is-mmm)  
   3.2. [Purpose of MMM](#32-purpose-of-mmm)  
   3.3. [Core Components of MMM](#33-core-components-of-mmm)  
   3.4. [Data Structure for MMM](#34-data-structure-for-mmm)  
   3.5. [How to Build an MMM](#35-how-to-build-an-mmm)  
   3.6. [MMM Libraries](#36-mmm-libraries)  
   3.7. [When to Use MMM](#37-when-to-use-mmm)  


---

## 4. Marketing Attribution & MMM

---

### 1. Attribution vs. MMM – Quick Comparison

| Aspect                     | Attribution                          | Marketing Mix Modeling (MMM)             |
|----------------------------|---------------------------------------|-------------------------------------------|
| What it does               | Assign credit to marketing touchpoints | Quantify incremental sales from media     |
| Granularity                | User/session-level                    | Time-aggregated (e.g., daily revenue)     |
| Main input                 | Clickstream/journey data              | Media spend + sales time series           |
| Output                     | Conversion share by channel           | ROI, media lift, marginal return curves   |
| Techniques used            | Heuristics, Markov, Shapley, uplift   | Regression, adstock, saturation, Bayesian |
| Ideal for                  | Channel optimization, bidding logic   | Strategic planning and budget forecasting |

- Use **attribution models for tactical insights** (e.g., channel-level ROAS)  
- Use **MMM for strategic budgeting** across channels, including offline spend. Also to estimate long-term brand/media effect.

---

### 2. Attribution Modeling

---

#### 2.1 What Is Attribution?

**Definition**:  
Attribution is the process of **assigning credit** for a conversion to the various **marketing touchpoints** a user interacts with on their journey.

**Purpose**:
- Understand how each channel contributes to a conversion
- Optimize budget and bidding strategies across paid search, display, etc.
- Identify high- vs. low-impact user interactions

---

#### 2.2 Types of Attribution Models

**Rule-Based Models**
- **Last Click**: All credit to the final touchpoint before conversion
- **First Click**: All credit to the first interaction
- **Linear**: Equal credit to all touchpoints
- **Time Decay**: More credit to more recent touches
- **Position-Based**: Weighted split (e.g., 40-40-20: first, last, middle)

**Data-Driven Models for MTA**
- Model-based methods that assign value across the customer journey
- Use data-driven techniques (logistic regression, tree models) to predict conversion likelihood from sequences
- Can integrate with Shapley or Markov to improve interpretability

- **Logistic Regression Attribution**: Estimate probability of conversion given channels seen
  
- **Markov Chain Attribution**:
  - Model user paths as state transitions (also called **Markov process**)
  - It treats the process like a **probabilistic system**:
> "What’s the probability that a user moves from one channel to another — and eventually converts?"
  - Calculates removal effect: how conversion probability drops when a channel is removed
  - Good for capturing **path dependencies** and **drop-off behavior**

    **🧮 Steps in Markov Chain Attribution:**

    **✅ Step 1: Create Touchpoint Paths**

            Example input:

            | User | Journey                          | Converted |
            |------|----------------------------------|-----------|
            | U1   | Facebook → Email → Search        | Yes       |
            | U2   | Instagram → Direct               | No        |
            | U3   | Email → Search                   | Yes       |

    **✅ Step 2: Define the States:**

            - Each touchpoint (channel) is a **state**
            - Add two absorbing states:
              - **Conversion** (success)
              - **Null/Dropout** (failure)

    **✅ Step 3: Build the Transition Matrix**

            Calculate the **probability of moving** from one touchpoint to another.

            Example:
            
            | From → To     | Email | Search | Conversion |
            |---------------|-------|--------|------------|
            | Facebook      | 0.5   | 0.3    | 0.2        |
            | Email         | 0.0   | 0.6    | 0.4        |
            | Search        | 0.0   | 0.0    | 1.0        |
            
            - Each row sums to 1
            - These are **transition probabilities**

    **✅ Step 4: Calculate Removal Effect**  

            For each channel:
            1. **Remove the channel** from the model
            2. Recalculate conversion rate from all paths
            3. Compute the **drop in total conversions**
            4. That drop = the **value** of the removed channel
            
            This answers:
            > “If we removed channel X, how many fewer conversions would we expect?”

    **📈 Output: Channel Attribution Scores**

            After computing **removal effects** for all channels, normalize them so that:
            - The sum = 100% of conversions
            - Each channel gets a **proportional credit**

    **🧰 Strengths**

        - Captures **assistive value** (e.g., first touch, mid funnel)
        - Accounts for **channel interdependencies**
        - Reflects **real sequences**, not just positions

    **⚠️ Limitations**  

        - Doesn’t capture **incrementality** — only **path dependency**
        - Doesn’t account for **external effects** (e.g., pricing, promos)
        - Can be **computationally heavy** if you have long paths and many channels

---

- **Shapley Value Attribution**:
  - Based on cooperative game theory
  - Computes marginal contribution of each channel across all possible combinations
  - Often used in combination with machine learning models for explainability
 
    Two possible implementations:

    - **Pure standalone shapley values attribution:**  
      - Shapley fairly distributes credit for a conversion
      - It accounts for interaction: A channel may add more value when combined with others
      - **Computationally expensive**, especially with many channels

    - **Final layer over an Attribution machine learning model for explainability:**
      - Apply Shapley values to a trained model (e.g., tree-based model predicting conversion)
      - Shows feature importance per prediction
      - Used to explain why the model attributed value to specific channels
      - Much faster and scalable with libraries like SHAP

**IMPORTANT: SHAP Values only show CORRELATION, not CAUSALITY**   


**Uplift Modeling (Advanced)**
- Focuses on **incremental effect** of showing a touchpoint
- Requires experimental design (e.g., geo holdouts or A/B splits)
- Outputs **incremental ROAS** instead of attribution credit

---

#### 2.3 Data Structure for Attribution

**Structure**: User-level or session-level journey logs  
- One row per user/session/conversion event
- Includes:
  - Timestamps
  - Channel/campaign names
  - Conversion outcome (binary or value)
  - Optional: device, region, ad type, etc.

**Source**: Google Ads logs, GA4 exports, CRM clickstream logs

---

#### 2.4 How to Build Attribution Models

1. **Data Preparation**
   - Collect full paths: channel sequences per user
   - Encode path positions, time between touches, conversions

2. **Model Selection**
   - Choose from rule-based, Markov, Shapley, or uplift
   - For data-driven: fit conversion model with touchpoints as features

3. **Evaluation**
   - Backtest accuracy vs. observed conversions
   - Use metrics like AUC, uplift@K, AUUC, or ROAS correlation

4. **Application**
   - Inform bid adjustments
   - Identify top vs. assistive channels
   - Customize based on campaign type (e.g. generic vs. branded)

---

#### 2.5 How to Use ML + SHAP Attribution in Practice

**Step 1: Understand What You Have**

- You've trained a **conversion prediction model** (e.g. XGBoost, Logistic Regression)
- You've applied **SHAP** to break down each prediction into **feature contributions**
- For each user/session, you now have:
  - A predicted probability of conversion
  - A list of channels/features with their SHAP value (positive or negative)

**Step 2: Aggregate Insights Across Users**  

1. **Per Channel**:
   - Sum or average SHAP values for each channel
   - This gives you **global feature importance** → shows which channels are driving predictions

2. **Per Segment**:
   - Break down SHAP contributions by segment (e.g., device, geo, audience)
   - Identify where each channel is most effective

3. **Per User** (optional for personalization):
   - Identify which channels had the highest SHAP impact per user
   - Use this to build user-level targeting logic

**Step 3: Visualize & Explain**

- 📊 **Global Importance Plot**: Bar chart of average SHAP values per feature/channel
- 🌈 **SHAP Summary Plot**: Shows impact and distribution of features across predictions
- 🔍 **SHAP Force Plot**: Explains prediction for an individual user (great for debugging or execs)

**Step 4: Drive Marketing Actions**

| Insight                              | Action                                                               |
|--------------------------------------|----------------------------------------------------------------------|
| Channel A consistently has high SHAP | Increase bids or budgets on Channel A                                |
| Channel B has high impact in Germany | Geo-target more aggressively in that region                          |
| Mobile device = negative SHAP impact | Adjust mobile landing pages or UX                                    |
| Users seeing Email + Search convert better | Design retargeting journeys to trigger both channels           |
| SHAP shows some campaigns add no lift | Pause or reallocate those budget lines                               |

**Step 5: Integrate into Business Workflow**

- 💡 **Targeting**: Use SHAP to build **high-propensity segments**
- 🧪 **Testing**: Run A/B tests based on SHAP-defined segments (e.g., top vs. bottom 10%)
- 💬 **Stakeholder reporting**: Use SHAP values to justify spend, performance, or segmentation strategies
- ⚙️ **Automation**: Feed segment-level SHAP scores into bidding scripts or CRM logic

**Step 6: Monitor and Refine**

- Track **conversion lift** after making SHAP-based changes
- Retrain the model periodically as seasonality and behavior evolve
- Use SHAP drift to detect when feature contributions change

**✅ Summary**  

SHAP values **turn black-box ML models into actionable marketing insight** by:
- Quantifying **which features/channels drive conversions**
- Enabling **data-driven targeting and bidding**
- Providing **defensible insights** for budget reallocation

---

#### 2.5 Attribution Libraries

- `Shap`: Shapley values from tree-based or logistic models
- `markovify`, `networkx`: Build and visualize Markov chain attribution models
- `scikit-learn`: Logistic regression or tree models for MTA
- `scikit-uplift`, `econml`, `CausalML`: For uplift modeling approaches
- `lifetimes` (used sometimes in LTV estimation alongside attribution)


---

### 3. Marketing Mix Modeling (MMM)

---

#### 3.1 What Is MMM?

**Definition**:  
Marketing Mix Modeling (MMM) is a **statistical modeling technique** (usually regression-based) that quantifies the **incremental effect of media spend** on business outcomes (e.g., sales, conversions), while controlling for external and organic influences.

---

#### 3.2 Purpose of MMM

- Estimate **ROI** for each marketing channel
- Forecast **revenue or conversions** under different spend levels
- Account for:
  - **Baseline demand** (non-media-driven revenue)
  - **Adstock** (carryover effects of media over time)
  - **Saturation** (diminishing returns as spend increases)
  - **Seasonality**, **promos**, and other confounders

---

#### 3.3 Core Components of MMM

1. **Baseline Estimation**  
   - Captures organic demand (what would happen without media)
   - Can include trend, seasonality, competitor activity, etc.

2. **Adstock Transformation**  
   - Models delayed media impact over time  
   - Uses a **decay rate** to simulate memory of past impressions (Carry-over effect)
   - Replaces the raw ad spend per channel column.
   - Decay rate could geometric Adstock (simple decay rate) or Weibull decay (models delayed peak, used in Meta's Robyn).

3. **Saturation Function**  
   - Models diminishing returns to spend
   - Prevents the model from overestimating media impact at high spend
   - Reflects real-world ad fatigue, budget inefficiency, or reach limits
   - Works **together with adstock** to shape realistic response curves

   - **Common form:** Hill function (Used in Meta's Robyn) or log transformation (Simple & Naive)

4. **Media Coefficients**  
   - Quantifies marginal contribution of each channel
   - Can be converted to **ROI** or **marginal cost per conversion**
   - Use MMM coefficients or **Shapley values** to split total revenue into media-contributed vs. baseline

    - Shapley provides a model-agnostic way to allocate impact, by:
      1. Taking the trained MMM model
      2. Running channel inclusion/exclusion permutations
      3. Measuring the marginal effect of each channel on total predicted revenue

5. **Control Variables**  
   - Promotions, pricing changes, holidays, weather, competitor activity




---

#### 3.4 Data Structure for MMM

**Structure**: Time-series panel (e.g., daily or weekly aggregated data)

| Column Type         | Examples                                  |
|----------------------|--------------------------------------------|
| Target Variable       | Revenue, conversions, bookings            |
| Media Variables       | Spend or impressions per channel          |
| Transformed Media     | Adstocked, saturated versions of media    |
| Control Variables     | Pricing, holidays, weather, seasonality   |
| Time Index            | Date (day or week granularity)            |

**Optional Breakdown**:  
- Split by **region**, **product line**, or **market**  
- Hierarchical modeling allows for nesting (e.g., geo within country)

---

#### 3.5 How to Build an MMM

1. **Preprocess Your Data**
   - Aggregate spend, sales, and external drivers
   - Normalize or log-transform variables
   - Create adstocked versions of media variables
   - Apply saturation functions (Hill, logistic, etc.)

2. **Model Specification**
   - Typical: log-log model  
     \[
     \log(Y) = \beta_0 + \sum_i \beta_i \cdot \text{adstock}_i + \gamma Z + \epsilon
     \]

3. **Fit the Model**
   - Use linear regression, Bayesian regression, or ridge regression
   - Check R², MAPE, and holdout accuracy

4. **Decompose Revenue**
   - Separate predicted revenue into baseline vs. channel contributions
   - Calculate marginal ROI:  
     \[
     \text{mROI} = \frac{\Delta \text{Revenue}}{\Delta \text{Spend}}
     \]
     
   - Use Cases:

     1. Explain media ROI to finance/execs
     2. Benchmark media efficiency vs. baseline demand
     3. Track baseline growth independently of marketing
     4. Feed into **marginal ROI** or **diminishing return** curves

5. **Calibrate and Validate**
   - Even a statistically strong model can produce biased results if:
        - Data quality is poor
        - Key variables are missing
        - Media effects are over- or underestimated

    Validation ensures your model reflects **reality**, not just curve-fitting.

   **1. Holdout Validation**

    - **What**: Remove part of the time period or a region from training
    - **Why**: Test how well the model predicts **unseen data**
    - **How**:
      - Train model on e.g. 2023 Q1–Q3
      - Predict Q4 and compare to actuals
      - Use **MAPE** or **RMSE** for error evaluation

    **2. Geo Holdout Experiments (Calibrated Validation)**
    
    - **What**: Stop media in some geos, continue in others
    - **Why**: Observe true **incremental lift**
    - **How**:
      - Pause search ads in Berlin, keep running in Hamburg
      - Use DiD or Causal Impact to measure real-world effect
      - Calibrate MMM output to match observed geo lift

    **3. A/B Test Comparison**

    - **What**: Compare MMM-estimated lift to lift measured in an experiment
    - **Why**: Align modeled attribution with **ground truth**
    - **How**:
      - Run an A/B test on a promo or campaign
      - Check whether MMM predicts similar uplift
      - Adjust coefficients or weights if necessary

    **4. Confidence / Credible Intervals**

    - Especially important in **Bayesian MMM**
    - Output:
      - Range of likely ROI values per channel
      - 95% credible intervals help with **risk-adjusted decision making**
    - Use to:
      - Show uncertainty in media impact
      - Set **safe budgets** based on lower-bound ROI



    **📈 Recommended Outputs**

    | Channel | Mean ROI | 95% CI Lower | 95% CI Upper |
    |---------|----------|--------------|--------------|
    | TV      | 1.6      | 1.2          | 2.0          |
    | Search  | 3.4      | 2.8          | 4.2          |
    
    

     **📌 Summary**
    
    - ✅ Holdouts validate prediction accuracy
    - ✅ Geo & A/B tests anchor the model to real-world causality
    - ✅ Credible intervals quantify uncertainty and protect against overconfidence

---

#### ✅ Bayesian MMM
- Enhances traditional MMM with:
  - **Credible intervals**
  - Prior knowledge (e.g. plausible lift ranges)
  - Hierarchical modeling across markets or products
  
---

#### 3.6 MMM Libraries

- `Facebook Robyn` (R)  
  - Open-source MMM tool with automated adstock & saturation tuning  
  - Popular in the industry, often replicated in Python logic

- `causalimpact`  
  - Good for single intervention campaigns in time series  
  - Estimates lift from Bayesian structural time series

- `PyMC`, `pymc3`, `bayespy`  
  - Use for fully Bayesian MMM with priors and posterior inference

- `pandas`, `numpy`, `matplotlib`, `seaborn`  
  - Used for data cleaning, transformation, and diagnostics


---

#### 3.7 When to Use MMM

Use MMM when:
- You want **channel-level ROI** across online and offline media
- You need **strategic spend forecasting**
- Attribution data is unavailable (e.g., iOS restrictions, no user-level tracking)
- You're measuring long-term brand/media impact
- You’re combining spend, seasonality, and non-digital effects

---

### 🧰 Libraries:

- `Facebook Robyn` (R, but used in industry for MMM — alternative logic can be replicated in Python)
- `causalimpact` (intervention-based MMM)
- `bayespy`, `PyMC` (Bayesian MMM)
- `Shap` (Shapley values for explainability)
- `markovify`, `networkx` (custom Markov chain attribution models)
- `lifetimes` (used sometimes in LTV estimation alongside attribution)
- `pandas`, `numpy`, `matplotlib`, `seaborn`
