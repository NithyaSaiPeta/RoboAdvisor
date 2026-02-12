import numpy as np
import pandas as pd
from scipy.optimize import minimize


def mean_variance_optimization(
    returns: pd.DataFrame,
    risk_free_rate: float = 0.06,
    max_weight: float = 0.4
):
    mu = returns.mean() * 252
    cov = returns.cov() * 252
    n = len(mu)

    def neg_sharpe(weights):
        port_return = np.dot(weights, mu)
        port_vol = np.sqrt(np.dot(weights.T, np.dot(cov, weights)))
        return -(port_return - risk_free_rate) / port_vol

    # Constraints
    constraints = (
        {"type": "eq", "fun": lambda w: np.sum(w) - 1}
    )

    bounds = tuple((0, max_weight) for _ in range(n))

    init_guess = np.ones(n) / n

    result = minimize(
        neg_sharpe,
        init_guess,
        method="SLSQP",
        bounds=bounds,
        constraints=constraints
    )

    return pd.Series(result.x, index=returns.columns)
