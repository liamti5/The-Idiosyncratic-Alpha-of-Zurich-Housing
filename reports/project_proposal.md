# Research Proposal: The Idiosyncratic Alpha of Zurich Housing

**Author:** Liam Tessendorf  
**Institution:** Waseda University - Time Series Analysis  
**Date:** December 15, 2025

---

## 1 Research Question
Real estate prices are heavily influenced by national macroeconomic factors ("Beta"), such as interest rates and national growth, which often mask local market dynamics. This study adopts a factor-investing framework to isolate the idiosyncratic component ("Alpha") of the Zurich housing market.

1.  **Primary Research Question:** Can we successfully isolate and forecast the idiosyncratic price component $(\epsilon_{t})$ of the Zurich housing market after stripping out national macroeconomic factors?
2.  **Secondary Research Question:** Do local variables (e.g., net migration, vacancy rates) have predictive power over these isolated residuals, confirming that they represent true local supply/demand dynamics rather than noise?

---

## 2 Data
The dataset spans approx. **Q1 1980 – Q4 2024** (Quarterly, with interpolation for local data like migration and vacancy rates).

* **Target Asset ($Y_{t}$):** Zurich Housing Index (ZWEX).
* **Systematic Factors (Macro Beta):**
    * **Market:** IMPI (Swiss Residential Property Price Index).
    * **Rates:** 10-Year Swiss Confederation Bond Yields.
    * **Economic:** Swiss GDP Growth and CPI (Inflation).
* **Idiosyncratic Predictors (Local Alpha):** Canton of Zurich Net Migration and Vacancy Rates.

---

## 3 Methodology

### Phase I: The "Horse Race" Models (Specification)
Instead of stripping beta first, you define two competing models upfront. This avoids the inference error because you estimate parameters simultaneously.

**Model A (The "Beta-Only" Baseline):**
Assumes Zurich is just a proxy for Switzerland.
$$r_{Z,t} = \alpha + \beta_1 r_{National,t} + \beta_2 \Delta Rates_t + \beta_3 \Delta \text{RealGDP}_t + u_t$$

**Model B (The "Alpha + Beta" Joint Model):**
Assumes local factors add value conditional on macro factors.
$$r_{Z,t} = \alpha + \underbrace{\beta_{Macro}X_{Macro,t}}_{\text{Beta}} + \underbrace{\sum \gamma_i \text{Local}_{i,t-k}}_{\text{Alpha Drivers}} + \nu_t$$

**Note:** You still use Ridge Regression ($L_{2}$ regularization) here because now you have even more correlated variables (Macro + Local) in one equation.

Model C (AIC Selection): VAR

### Phase II: Inference & Causality (Proving Alpha Exists)
Since you are estimating jointly, you can now trust the p-values.

* **Bootstrapping:** Perform bootstrapping on the local coefficients ($\gamma$).
* **Granger Causality:** Run it within this joint framework to show that Migration leads Prices, controlling for GDP.

### Phase III: Forecast Evaluation (The Economic Value)
You compare the out-of-sample accuracy of Model A vs. Model B.

**The Logic:** "Does adding local complexity actually reduce forecast error?"

**Evaluation:**
* **RMSE** (Root Mean Squared Error).
* **Granger-Newbold Test**
* **Diebold-Mariano Test:** To see if the improvement from Model B is statistically significant.

---

## 4 Conclusion
This project aims to explain if and why Zurich diverges from the Swiss average. By successfully modeling $\epsilon_{t}$, we demonstrate that local policy and factors drive a measurable "Alpha" distinct from the national "Beta".