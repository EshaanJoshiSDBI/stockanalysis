# clustering based on price movements
from os import close
import pandas_datareader as web
import pandas as pd
import numpy as np
import datetime as dt
from yahoo_fin import stock_info as fin
from sklearn.preprocessing import Normalizer
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
companies_name = fin.tickers_niftybank()
companies = [i + '.NS' for i in companies_name]
start = dt.datetime.now() - dt.timedelta(days = 365 *2)
end = dt.datetime.now()
data = web.DataReader(list(companies),'yahoo',start,end)
open_values = np.array(data['Open'].T)
close_values = np.array(data['Close'].T)
daily_movements = close_values - open_values
norm = Normalizer()
cluster = KMeans(n_clusters=5,max_iter=1000)
pipe = make_pipeline(norm,cluster)
pipe.fit(daily_movements)
labels = pipe.predict(daily_movements)
res = pd.DataFrame({'labels':labels,'Tickers':list(companies)}).sort_values(by = ['labels'], axis = 0)
print(res)