import pandas as pd
from datetime import datetime as dt
# creating a function which downloads the stock data from the specified source
def create_DataFrame(company_name):
# The starting date from which the stock data is to be collected
    start_date = str(int(dt(2015,1,1).timestamp()))    
# The date till which the stock data is to be collected
    end_date = str(int(dt.now().timestamp()))
    data_link = 'https://query1.finance.yahoo.com/v7/finance/download/' + company_name + '.NS?period1='+ start_date + '&period2=' + end_date + '&interval=1d&events=history&includeAdjustedClose=true' 
    df_temp = pd.read_csv(data_link)
    df_temp.Date = pd.to_datetime(df_temp.Date)
    df_temp = df_temp.set_index('Date')
    df_temp = df_temp.fillna(df_temp.mean())
    return df_temp
    #print(df_temp)