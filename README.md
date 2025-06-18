SMA Crossover Strategy Backtest
This project implements a simple backtest of a trading strategy based on the crossover of two Simple Moving Averages (SMA): a short-term SMA (50-day) and a long-term SMA (200-day). The strategy goes long when the 50-day SMA crosses above the 200-day SMA and exits the position when the 50-day SMA drops below the 200-day SMA. It assumes long-only positions with no shorting.

Features
Downloads historical stock price data using the yfinance library
Calculates SMA-50 and SMA-200 for signal generation
Generates buy/sell signals and simulates strategy returns
Compares strategy performance with Buy & Hold
Plots:
Stock price with SMA overlays
Entry and exit points
Equity curve of strategy vs Buy & Hold
Strategy Logic
Calculate the 50-day and 200-day simple moving averages.
Generate a buy signal when SMA-50 > SMA-200.
Exit (sell to cash) when SMA-50 < SMA-200.
Track equity using daily returns while in position.
Avoid lookahead bias by shifting the position by one day.
