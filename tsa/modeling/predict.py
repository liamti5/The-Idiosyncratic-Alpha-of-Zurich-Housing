from typing import List, Tuple

import numpy as np
import pandas as pd
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import StandardScaler
from statsmodels.tsa.api import VAR


class ExpandingWindowForecaster:
    def __init__(self, initial_window: float = 0.6, random_state: int = 42):
        self.initial_window = initial_window
        self.random_state = random_state

    def ridge(
        self,
        data: pd.DataFrame,
        target_col: str,
        alpha_range: np.ndarray = np.logspace(-6, 6, 13),
    ) -> Tuple[np.ndarray, np.ndarray, List[pd.Timestamp]]:
        np.random.seed(self.random_state)

        n = len(data)
        initial_size = int(n * self.initial_window)

        X = data.drop(columns=[target_col])
        y = data[target_col]

        predictions = []
        actuals = []
        forecast_index = []

        for t in range(initial_size, n):
            X_train = X.iloc[:t]
            y_train = y.iloc[:t]
            X_test = X.iloc[[t]]

            scaler = StandardScaler()
            X_train_scaled = scaler.fit_transform(X_train)
            X_test_scaled = scaler.transform(X_test)

            model = RidgeCV(alphas=alpha_range)
            model.fit(X_train_scaled, y_train)

            predictions.append(model.predict(X_test_scaled)[0])
            actuals.append(y.iloc[t])
            forecast_index.append(data.index[t])

        return np.array(predictions), np.array(actuals), forecast_index

    def var(
        self,
        data: pd.DataFrame,
        target_col: str,
        max_lag: int = 8,
    ) -> Tuple[np.ndarray, np.ndarray, List[pd.Timestamp]]:
        np.random.seed(self.random_state)

        n = len(data)
        initial_size = int(n * self.initial_window)
        target_idx = list(data.columns).index(target_col)

        predictions = []
        actuals = []
        forecast_index = []

        for t in range(initial_size, n):
            train_data = data.iloc[:t]

            model = VAR(train_data)
            try:
                lag_order = model.select_order(maxlags=min(max_lag, len(train_data) // 3)).aic
                lag_order = max(1, lag_order)
            except Exception:
                lag_order = 1

            var_fitted = model.fit(lag_order)
            forecast = var_fitted.forecast(train_data.values[-lag_order:], steps=1)

            predictions.append(forecast[0, target_idx])
            actuals.append(data.iloc[t][target_col])
            forecast_index.append(data.index[t])

        return np.array(predictions), np.array(actuals), forecast_index
