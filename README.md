# The Idiosyncratic Alpha of Zurich Housing: Separating Macro Beta from Local Dynamics

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

This is the code for my final project for the Time Series Analysis course at Waseda University. This study investigates the divergence of Zurich housing prices from the Swiss national average over the period 1980-2024. By employing a factor-investing framework, we decompose housing returns into a systematic national component (Macro Beta) and an idiosyncratic local component (Zurich Alpha). To address the high degree of multicollinearity among macroeconomic factors, we utilize Ridge Regression ($L_2$ regularization), which successfully isolates a stationary residual series representing local price dynamics. Our results indicate that local supply constraints, specifically vacancy rates, are the primary driver of this idiosyncratic Alpha, whereas demand-side migration flows lack significant predictive power. Furthermore, out-of-sample forecasting tests reveal that a penalized Ridge model achieves a 10.1\% lower Mean Squared Error (MSE) than a dynamic Vector Autoregression (VAR) model, underscoring the importance of regularization in modeling noisy real estate data.

## Project Organization

```
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         tsa and configuration for tools like black
│
└── tsa   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes tsa a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │
    └── plots.py                <- Code to create visualizations
```

## Prerequisites

- **Python 3.13+** (specified in `pyproject.toml`)
- **[uv](https://docs.astral.sh/uv/)** - Fast Python package installer and resolver

### Installing uv

If you don't have `uv` installed:

**macOS/Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Homebrew:**
```bash
brew install uv
```

**Windows:**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**With pip:**
```bash
pip install uv
```
if none of these options work, check the [installation guide](https://docs.astral.sh/uv/getting-started/installation/#standalone-installer).

## Quick Start

### 1. Clone the Repository

```bash
git@github.com:liamti5/The-Idiosyncratic-Alpha-of-Zurich-Housing.git
cd The-Idiosyncratic-Alpha-of-Zurich-Housing
```

### 2. Sync Dependencies

The `uv.lock` file ensures reproducible installations. Run:

```bash
uv sync
```

This will:
- Create a virtual environment (if not present)
- Install all dependencies with exact versions from `uv.lock`
- Set up the project in development mode


### 3. Launch Jupyter Notebook

```bash
uv run jupyter notebook
```

### 4. Notebook descriptions
1. `1.0_data-exploration-and-combine-data.ipynb` contains the inital data exploration and is where the data gets combined into one dataframe.
2. `1.1_stationarity-cointegration-structuralchange-check.ipynb` is where we check for stationarity, and make changes to the variables to ensure stationarity and enable future modelling.
3. `2.0-ridge-regression.ipynb` contains the two Ridge Regressions, as well as bootstrapping, confidence interval calculation and prediction.
4. `2.1-VAR.ipynb` contains the VAR model and its predictions.
5. `3.0-model-comparison.ipynb` is where the Ridge Regressions and VAR models are compared on their performance. 


