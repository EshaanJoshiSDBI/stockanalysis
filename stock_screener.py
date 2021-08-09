import pandas as pd
import pandas_datareader as web
import datetime as dt
from yahoo_fin import stock_info as fin
returns_list = []
tickers = fin.tickers_nifty50()
start = dt.datetime.now() - dt.timedelta(days = 365)
end = dt.datetime.now()
df = web.DataReader('^GSPC','yahoo',start,end)
df['Pct_change'] = df['Adj Close'].pct_change()
nifty_return = (df['Pct_change'] + 1).cumprod()[-1]
lst = []
df_final = pd.DataFrame(columns=['Ticker','Latest_price','Compare_Score','P/E ratio','PEG ratio','Moving 150','Moving 200','52_low','52_high'])
counter = 0
for ticker in tickers:
    if ticker == 'MM.NS':
        pass
    else:
        df_new = web.DataReader(ticker,'yahoo',start,end)
        df_new.to_csv(f'stock_data/{ticker}.csv')
        df_new['Pct_change'] = df_new['Adj Close'].pct_change()
        s_return = (df_new['Pct_change'] + 1).cumprod()[-1]
        returns = round((s_return / nifty_return), 2)
        returns_list.append(returns)
    counter+=1
    if counter == 5:
        break

best_performers = pd.DataFrame(list(zip(tickers,returns_list)),columns = ['Tickers','Returns_Compared'])
best_performers['Score'] = best_performers['Returns_Compared'].rank(pct=True) * 100
best_performers = best_performers[best_performers['Score'] >= best_performers['Score'].quantile(0.7)]
for ticker in best_performers['Tickers']:
    try:
        df_s = pd.read_csv(f'stock_data/{ticker}.csv',index_col=0)
        moving_avg = [150,200]
        for i in moving_avg:
            df_s['SMA_' + str(i)] = round(df_s['Adj Close'].rolling(windows = i).mean(),2)
        latest_price = df_s['Adj Close'][-1]
        pe_ratio = float(fin.get_quote_table(ticker)['PE Ratio (TTM)'])
        peg_ratio = float(fin.get_stats_valuation(ticker)[1][4])
        moving_avg_150 = df_s['SMA_150'][-1]
        moving_avg_200 = df_s['SMA_200'][-1]
        low_52 = round(min(df_s['Low'][-(52*5):]),2)
        high_52 = round(max(df_s['Low'][-(52*5):]),2)
        score = round(best_performers[best_performers['Ticker'] == ticker]['Score'].tolist()[0])
        ###
        condition_1 = latest_price > moving_avg_150 > moving_avg_200
        condition_2 = latest_price >= (1.3)*low_52
        condition_3 = latest_price >= (0.75)*high_52
        condition_4 = pe_ratio < 40
        condition_5 = peg_ratio < 2
        if condition_4 and condition_5:
            df_final = df_final.append({'Ticker':ticker,'Latest_price':latest_price,'Compare_Score':score,'P/E ratio':pe_ratio,'PEG ratio':peg_ratio,'Moving 150':moving_avg_150,'Moving 200':moving_avg_200,'52_low':low_52,'52_high':high_52},ignore_index = True)
    except Exception as e:
        print(f'{e} for {ticker}')
df_final.sort_values(by = 'Compare_Score',ascending = False)
pd.set_option('display.max_columns',10)
print(df_final)
df_final.to_csv('Final.csv')