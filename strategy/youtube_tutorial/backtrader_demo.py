
from backtrader import Cerebro
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Define the parameters
symbol = 'AAPL'  # Example stock symbol (Apple Inc.)
start_date = '2022-01-01'
end_date = '2022-12-31'
window = 50  # The window size for the moving average

# Download historical stock data from Yahoo Finance
data = yf.download(symbol, start=start_date, end=end_date)

# Calculate the Simple Moving Average (SMA)
data['SMA'] = data['Close'].rolling(window=window).mean()

# Plot the closing price and SMA
plt.figure(figsize=(10, 6))
plt.plot(data['Close'], label='Closing Price')
plt.plot(data['SMA'], label='SMA ({}-day)'.format(window))
plt.xlabel('Date')
plt.ylabel('Price')
plt.title('{} Stock Price with SMA'.format(symbol))
plt.legend()
plt.grid(True)
plt.show()

# def


if __name__ == '__main__':
    cerebro = Cerebro()





    cerebro.run()
    cerebro.plot()