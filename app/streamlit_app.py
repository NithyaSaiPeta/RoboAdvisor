import streamlit as st
from src.risk_profiling import get_risk_profile
from src.data_loader import load_price_data, compute_returns
from src.portfolio_optimization import mean_variance_optimization
from src.backtesting import backtest_portfolio

st.title("📊 Robo-Advisor: Portfolio Recommendation System")

st.sidebar.header("Investor Profile")

age = st.sidebar.number_input("Age", 18, 80, 25)
income = st.sidebar.number_input("Annual Income (₹)", 200000, 5000000, 1200000)
horizon = st.sidebar.number_input("Investment Horizon (years)", 1, 30, 10)
risk_tol = st.sidebar.slider("Risk Tolerance", 1, 5, 3)

user = {
    "age": age,
    "annual_income": income,
    "investment_horizon": horizon,
    "risk_tolerance": risk_tol
}

profile = get_risk_profile(user)

st.subheader("Risk Profile")
st.write(profile)

tickers = [
    # "HDFCBANK.NS",
    # "ICICIBANK.NS",
    # "INFY.NS",


    # # Large-cap stocks
    # "RELIANCE.NS",
    # "SBIN.NS",
    # "AXISBANK.NS",
    # "KOTAKBANK.NS",

    # # IT stocks
    # "HCLTECH.NS",
    # "WIPRO.NS",
    # "TECHM.NS",
    # "LTIM.NS",

    # # Pharma
    # "SUNPHARMA.NS",
    # "DRREDDY.NS",

    # Energy & Infra
    "ONGC.NS",
    "NTPC.NS",
    "POWERGRID.NS",

    # ETFs
    "NIFTYBEES.NS",
    "BANKBEES.NS",
    "JUNIORBEES.NS"
]


prices = load_price_data(tickers)
returns = compute_returns(prices)

weights = mean_variance_optimization(returns)

st.subheader("Optimal Portfolio Weights")
st.bar_chart(weights)

portfolio_returns, cumulative_returns, metrics = backtest_portfolio(
    returns, weights
)

st.subheader("Portfolio Performance Metrics")
st.json(metrics)

st.subheader("Cumulative Returns")
st.line_chart(cumulative_returns)
