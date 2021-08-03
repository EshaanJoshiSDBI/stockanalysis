# Libraries used
- Pandas
- Pandas datareader
- Numpy
- datetime
- matplotlib.pyplot
- mplfinance
- os
- yahoo fin
- Sklearn
- tkinter
- Re
- Plotly
# Modules
## RSI.py
- Plots the Relative Strength Index (RSI) which is the magnitude of recent price changes used to evaluae overbought or oversold conditions in the price of the asset.
## candlestickgraph.py
- Plots a candlestick graph for the chosen stock, shows volumes, ups and downs in the price using candlestick graph.
## clustering.py
- Forms clusters of stocks based on their moving averages.
## dropdown.py
- Used to make a gui where user can choose the stock, which attribute they want to specifically analyse and number of days for which they want to predict the price for.
## file_reader.py
- creates a dataframe after some data wrangling of the stock chosen by user.
## graphs.py
- Plots a graph of the attribute chosen by the user.
## interact_graph.py
- Creates an interactive candlestick graph which the user can interact with(zoomin/out, checking the prices by hovering over the candle,etc) in the form of an html file.
## predictions_module.py
- Predicting the prices of the stock using DecisionTreeRegressor and LinearRegression.