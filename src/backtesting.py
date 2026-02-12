import pandas as pd
import numpy as np
from src.metrics import sharpe_ratio, max_drawdown, cvar


def backtest_portfolio(returns: pd.DataFrame, weights: pd.Series):
    portfolio_returns = returns @ weights
    cumulative_returns = (1 + portfolio_returns).cumprod()

    metrics = {
        "CAGR": cumulative_returns.iloc[-1] ** (252 / len(cumulative_returns)) - 1,
        "Volatility": portfolio_returns.std() * np.sqrt(252),
        "Sharpe Ratio": sharpe_ratio(portfolio_returns),
        "Max Drawdown": max_drawdown(cumulative_returns),
        "CVaR (5%)": cvar(portfolio_returns)
    }

    return portfolio_returns, cumulative_returns, metrics