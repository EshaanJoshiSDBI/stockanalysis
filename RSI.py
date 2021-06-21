import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
def RSI(name,para_df):
    delta = para_df['Adj Close'].diff(1)
    delta.dropna(inplace = True)
    postive = delta.copy()
    negative = delta.copy()
    postive[postive < 0] = 0
    negative[negative > 0] = 0
    avg_profit = postive.rolling(window = 7).mean()
    avg_loss = abs(negative.rolling(window = 7).mean())
    rel_strength = avg_profit/avg_loss
    RSI = 100.0 - (100.0 / (1.0 + rel_strength))
    df = pd.DataFrame()
    df['Adj Close'] = para_df['Adj Close']
    df['RSI'] = RSI
    plt.figure(figsize = (16,25))
    plt_ = plt.subplot(211)
    plt_.plot(df.index,df['Adj Close'])
    plt.title("Adjusted Close Price for {}".format(name),color = 'white')
    plt_.grid(True, color = 'white')
    plt_.set_axisbelow(True)
    plt_.set_facecolor('black')
    plt_.figure.set_facecolor('black')
    plt_.tick_params(axis = 'x',colors = 'white')
    plt_.tick_params(axis = 'y',colors = 'white')
    plt.figure(figsize = (27,36))
    plt1 = plt.subplot(212,sharex = plt_)
    plt1.plot(df.index, df['RSI'], color = 'white')
    plt1.set_title('RSI for {}'.format(name),color = 'white')
    plt1.axhline(0, linestyle = '--',alpha = 0.5, color = 'red')
    plt1.axhline(10, linestyle = '--',alpha = 0.5, color = 'yellow')
    plt1.axhline(20, linestyle = '--',alpha = 0.5, color = 'green')
    plt1.axhline(30, linestyle = '--',alpha = 0.5, color = 'grey')
    plt1.axhline(70, linestyle = '--',alpha = 0.5, color = 'grey')
    plt1.axhline(80, linestyle = '--',alpha = 0.5, color = 'green')
    plt1.axhline(90, linestyle = '--',alpha = 0.5, color = 'yellow')
    plt1.axhline(100, linestyle = '--',alpha = 0.5, color = 'red')
    plt1.set_axisbelow(True)
    plt1.set_facecolor('black')
    plt1.tick_params(axis = 'x', color = 'white')
    plt1.tick_params(axis = 'y',color = 'white')
    plt.show()