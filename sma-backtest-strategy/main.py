import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

ticker = "AAPL"
start_date = "2020-01-01"
end_date = "2024-12-31"

df = yf.download(ticker, start=start_date, end=end_date)
df = df[['Close']]

df['SMA_50'] = df['Close'].rolling(window=50).mean()
df['SMA_200'] = df['Close'].rolling(window=200).mean()

df['Signal'] = 0
df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1
df['Position'] = df['Signal'].shift()


df['Daily Return'] = df['Close'].pct_change()
df['Strategy Return'] = df['Daily Return'] * df['Position']
initial_cash = 100000
df['Equity'] = initial_cash * (1 + df['Strategy Return']).cumprod()

df['Trade Signal'] = df['Position'].diff()

buy_signals = df[df['Trade Signal'] == 1]   
sell_signals = df[df['Trade Signal'] == -1]

plt.figure(figsize=(16, 8))
plt.plot(df['Close'], label='Close Price', alpha=0.5)
plt.plot(df['SMA_50'], label='SMA 50', linestyle='--', alpha=0.6)
plt.plot(df['SMA_200'], label='SMA 200', linestyle='--', alpha=0.6)

plt.scatter(buy_signals.index, buy_signals['Close'], marker='^', color='green', label='Buy Signal', s=100)

plt.scatter(sell_signals.index, sell_signals['Close'], marker='v', color='red', label='Sell Signal', s=100)

plt.title(f"{ticker} - SMA Backtesting ")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("example_output.png")
plt.show()