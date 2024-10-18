import yfinance as yf
start_date = '1990-01-01'
end_date = '2021-07-12'
data = yf.download("aapl", '1990-01-01', '2021-07-12')

data.tail()
data.dividends