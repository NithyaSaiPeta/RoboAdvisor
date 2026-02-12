from src.risk_profiling import get_risk_profile
from src.data_loader import load_price_data, compute_returns
from src.portfolio_optimization import mean_variance_optimization
from src.backtesting import backtest_portfolio

# 1️⃣ Test risk profiling
user = {
    "age": 26,
    "annual_income": 1200000,
    "investment_horizon": 10,
    "risk_tolerance": 4
}

profile = get_risk_profile(user)
print("Risk Profile:", profile)

# 2️⃣ Test data loading
tickers = ["HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS"]
prices = load_price_data(tickers)
returns = compute_returns(prices)

print("Price data shape:", prices.shape)
print("Returns shape:", returns.shape)

# 3️⃣ Test optimization
weights = mean_variance_optimization(returns)
print("Optimized Weights:")
print(weights)

# 4️⃣ Test backtesting
port_rets, cum_rets, metrics = backtest_portfolio(returns, weights)
print("Metrics:")
for k, v in metrics.items():
    print(f"{k}: {v}")
