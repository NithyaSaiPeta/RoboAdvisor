import numpy as np
import pandas as pd


def sharpe_ratio(returns, risk_free_rate=0.06):
    excess = returns.mean() * 252 - risk_free_rate
    vol = returns.std() * np.sqrt(252)
    return excess / vol


def max_drawdown(cumulative_returns):
    rolling_max = cumulative_returns.cummax()
    drawdown = cumulative_returns / rolling_max - 1
    return drawdown.min()


def cvar(returns, alpha=0.05):
    return np.mean(returns[returns <= returns.quantile(alpha)])
