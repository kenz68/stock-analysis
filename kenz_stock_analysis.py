from numpy.lib.npyio import load
import pandas as pd
import datetime as dt
import pandas_datareader.data as web
from pandas import Series, DataFrame
from vnquant.DataLoader import DataLoader
import matplotlib.pyplot as plt

start = dt.datetime(2021, 1, 1)
end = dt.datetime(2021, 6, 1)

data_netflix = web.DataReader("NFLX", 'yahoo', start, end)
print(data_netflix.tail())

loader = DataLoader(symbols='VIC',
                    start='2021-01-01',
                    end='2021-06-01',
                    minimal=False,
                    data_source='vnd')

data_vic = loader.download()
print(data_vic.head())

loader = DataLoader(symbols='HVN',
                    start='2021-01-01',
                    end='2021-06-01',
                    minimal=False,
                    data_source='vnd')
data_hvn = loader.download()
print(data_hvn.tail())

data_netflix['Open'].plot(label='netflix', figsize=(15,10), title='open')

fig, ax = plt.subplots(figsize=(15, 10))
ax.plot(data_hvn['open'], label='VN-airlines')
ax.plot(data_vic['open'], label='Vincommerce')
ax.set_xlabel('Date')
ax.set_title('open')
plt.legend()