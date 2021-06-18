import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import pandas_datareader as web
import numpy as np
import os
import time
import yfinance as yf
from dateutil.relativedelta import relativedelta
import matplotlib.pyplot as plt

# # deletes the folder where the stocks data are stored
# shutil.rmtree(
#     "<path to this project>/Stocks")
# # makes the folder where the stocks data are stored
# os.mkdir("<path to this project>/Stocks")

# reads the excel file you created representing your portfolio
df = pd.read_excel(
    r"C:\Users\Paul\AppData\Local\Programs\Python\Python38-32\SGH\prog_py\SGH\Project\Portfolio\LT_Portfolio.xlsx")
# converts the stocks and their weights to a pandas dataframe
tickers = df.to_dict()

# print(df.head())

# converts the date from a TimeStamp format to a string so that it is usable
j = 0
for k in tickers['Purchase Date']:
    tickers['Purchase Date'][j] = tickers['Purchase Date'][j].strftime(
        '%Y-%m-%d')
    j += 1

# number of stocks not downloaded
stocks_not_donwloaded = 0
# used for iteration
i = 0
#
# loop used for iteration through each ticker to collect the data
while (i < len(tickers['Ticker'])):
    try:
        # stores each ticker in your portfolio one by one as we go through the loop
        stock = tickers['Ticker'][i]
        temp = yf.Ticker(str(stock)+".JO")
        # gets the historical data for the specific ticker
        data = temp.history(period="max")
        # stores the data to our folder in .csv format
        data.to_csv(
            r"C:\Users\Paul\AppData\Local\Programs\Python\Python38-32\Coursera\Week1\Portfolio\Stocks\Stocks"+stock+".csv")
        # slows the script down a bit in order to not make very fast requests to the yahoo API
        time.sleep(1)
        i += 1
    except ValueError:
        # if there is an error downloading data print the name of that ticker
        print("Error with Downloading Data for " + stock)
        i = +1
print("Stocks Successfully Imported" + str(i - stocks_not_donwloaded))

# ANH = pd.read_csv("Stocks\\StocksANH.csv")
# IPF = pd.read_csv("Stocks\\StocksIPF.csv")
# NPN = pd.read_csv("Stocks\\StocksNPN.csv")
# PRX = pd.read_csv("Stocks\\StocksPRX.csv")
# RNI = pd.read_csv("Stocks\\StocksRNI.csv")
# TCP = pd.read_csv("Stocks\\StocksTCP.csv")
# VOD = pd.read_csv("Stocks\\StocksVOD.csv")
#
# # print(ANH.head())
# # print(ANH.describe())
#
# df = pd.read_excel(
#     r"C:\Users\Paul\AppData\Local\Programs\Python\Python38-32\Coursera\Week1\LT_Portfolio.xlsx")
# # converts the stocks and their weights to a pandas dataframe
# tickers = df.to_dict()
#
# j = 0
# for k in tickers['Purchase Date']:
#     tickers['Purchase Date'][j] = tickers['Purchase Date'][j].strftime(
#         '%Y-%m-%d')
#     j += 1
#
# def volatility(stock_data):
#     ''' Calculate the Annualized Volatility of a Trading Strategy '''
#     volatility = stock_data['Return'].std() * np.sqrt(52)
#
#     return volatility
#
#
# def CAGR(stock_data):
#     ''' Calculate the Compound Annual Growth Rate of a Trading Strategy '''
#     stock_data['Cumulative_Return'] = (1 + stock_data['Return']).cumprod()
#     years = len(stock_data) / 52
#     carg = stock_data['Cumulative_Return'].tolist()[-1] ** (1 / years) - 1
#
#     return carg
#
#
# def sharpe_ratio(stock_data, risk_free):
#     ''' Calculate the Sharpe Ratio of a Portfolio '''
#     sharpe = (CAGR(stock_data) - risk_free) / volatility(stock_data)
#
#     return sharpe
#
# def sortino_ratio(Stock_data, N,rf):
#     mean = Stock_data.mean() * N -rf
#     std_neg = Stock_data[Stock_data<0].std()*np.sqrt(N)
#     return mean/std_neg
#
# def max_drawdown(return_series):
#     comp_ret = (return_series+1).cumprod()
#     peak = comp_ret.expanding(min_periods=1).max()
#     dd = (comp_ret/peak)-1
#     return dd.min()
#
#
# ''' Downloading Historical Stock Data for all DJI Stocks '''
# start = dt.datetime(2018, 1, 1)
# end = dt.datetime(2021,4, 1)
# port_data = {}
#   # array to store the stock data files
#
# # stores each directory in the 'list_files' array
# ticker_list = list(tickers['Ticker'].values())
# # for stock in ticker_list:
# #     port_data[stock]= (r"C:\Users\Paul\AppData\Local\Programs\Python\Python38-32\Coursera\Week1\Portfolio\Stocks\Stocks" + stock + ".csv")
# # print(port_data)
# for stock in ticker_list:
#     print(f'Downloading stock data for {stock+".JO"}')
#     port_data[stock] = web.get_data_yahoo(stock+".JO", start, end, interval = 'w')
#     print(f'{stock+".JO"} downloaded...')
#
# Benchmark = web.get_data_yahoo("^J200.JO", start, end, interval = 'w')
#
# ''' Calculating the weekly returns of all DJI Stocks '''
# port_returns = pd.DataFrame()
#
# for stock in ticker_list:
#     print(f'Calculating the weekly return for {stock}')
#     port_returns[stock] = port_data[stock]['Close'].pct_change().dropna()
#
# print(port_returns)
#
#
#
#
# def portfolio(dataframe, n_stocks, n_remove):
#     '''
#     dataframe: Dataframe with the stocks returns
#     n_stocks: Number of stocks to be selected in the portfolio
#     n_remove: Number of bad stocks to be remove in the portfolio
#     '''
#     portfolio = []
#     weekly_return = [0]
#     for i in range(1, len(dataframe)):
#         if len(portfolio) > 0:
#             weekly_return.append(dataframe[portfolio].iloc[i, :].mean())
#             negative_stocks = dataframe[portfolio].iloc[i, :].sort_values(ascending=True)[: n_remove].index.tolist()
#             portfolio = [stock for stock in portfolio if stock not in negative_stocks]
#         to_fill = n_stocks - len(portfolio)
#         new_stocks = dataframe.iloc[i, :].sort_values(ascending=False)[:n_stocks].index.tolist()
#         new_stocks = [stock for stock in new_stocks if stock not in portfolio][
#                      :to_fill]  # We make sure to not repeat stocks in the portfolio
#         portfolio = portfolio + new_stocks
#         # print(f'The weekly portfolio selected is {portfolio}')
#
#     portfolio_ret = pd.DataFrame(np.array(weekly_return), columns=['Return'])
#     return portfolio_ret
#
# # print(portfolio(port_returns,8,0))
# portfolio = portfolio(port_returns,8,0)

# Benchmark['Return'] = Benchmark['Close'].pct_change()
# Benchmark.dropna(inplace=True)
#
# print(f'The Compound Annual Growth Rate is {CAGR(portfolio)}')
# print(f'The Portfolio Volality is {volatility(portfolio)}')
# print(f'The Sharpe Ratio is {sharpe_ratio(portfolio, 0.05)}')
# print(f'The Sortino Ratio is {sortino_ratio(portfolio,250, 0.05)}')
# print(f'The Max Drawdown is {max_drawdown(portfolio)}')
#
#
#
# print(f'The Compound Annual Growth Rate is {CAGR(Benchmark)}')
# print(f'The Index Volality is {volatility(Benchmark)}')
# print(f'The Sharpe Ratio is {sharpe_ratio(Benchmark, 0.05)}')
# print(f'The Sortino Ratio is {sortino_ratio(Benchmark,250, 0.05)}')
# print(f'The Max Drawdown is {max_drawdown(Benchmark)}')

# ''' Visualization '''
# fig, ax = plt.subplots(figsize = (20, 10))
# plt.plot((1 + portfolio['Return']).cumprod(), color = 'g')
# plt.plot((1 + Benchmark['Return'][2:].reset_index(drop = True)).cumprod(), color = 'r')
# plt.title('Top40 Return vs Portfolio Return', fontsize = 20)
# plt.ylabel('Cumulative Return', fontsize = 20)
# plt.xlabel('Week', fontsize = 20)
# plt.xticks(fontsize = 15)
# plt.yticks(fontsize = 15)
# ax.legend(['Strategy Return', 'Top40 Return'], fontsize = 15)
# plt.subplots_adjust(top = 0.92, bottom = 0.1, left = 0.08, right = 0.94)
# plt.show()