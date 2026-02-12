# AI-Driven Robo-Advisor with Portfolio Optimization
An end-to-end robo-advisory system that generates personalized investment portfolios based on investor risk profiles, forecasts asset returns using LSTM, and optimizes portfolios using Modern Portfolio Theory and Monte Carlo simulations.

Features:
- Risk profiling to convert user attributes into a continuous risk score
- Investor segmentation into risk profiles (Conservative, Moderate, Aggressive, etc.)
- LSTM-based price & return forecasting
- Achieved **26% lower RMSE (15.73 INR)** vs ARIMA baseline
- Long-only portfolio optimization using:
  - Predicted returns
  - Modern Portfolio Theory (MPT)
  - Monte Carlo simulations
- Portfolio selection by **maximizing Sharpe Ratio**

Tech Stack:
- Python, Pandas, NumPy
- Scikit-learn
- TensorFlow / PyTorch (LSTM)
- Matplotlib / Seaborn





