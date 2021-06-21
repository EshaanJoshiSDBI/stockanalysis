import matplotlib.pyplot as plt
import mplfinance as mpl
def plot(attribute,company,name):
    def open_(company):
        plt.figure(figsize=(25,9))
        company['Open'].plot()
        plt.xlabel(None)
        plt.ylabel('Open')
        plt.title(name)
        plt.show()
    def close_(company):
        plt.figure(figsize=(25,9))
        company['Close'].plot()
        plt.xlabel(None)
        plt.ylabel('Close')
        plt.title(name)
        plt.show()
    def high_(company):
        plt.figure(figsize=(25,9))
        company['High'].plot()
        plt.xlabel(None)
        plt.ylabel('High')
        plt.title(name)
        plt.show()
    def low_(company):
        plt.figure(figsize=(25,9))
        company['Low'].plot()
        plt.xlabel(None)
        plt.ylabel('Low')
        plt.title(name)
        plt.show()
    def vol_(company):
        plt.figure(figsize=(25,9))
        company['Volume'].plot()
        plt.xlabel(None)
        plt.ylabel('Volumes')
        plt.title(name)
        plt.show()
    def all_(company):
        mpl.plot(company,type = 'line',
                figratio = (20,12),
                volume = True,
                tight_layout = True)
    if attribute == 'Open':
        open_(company)
    elif attribute == 'Close':
        close_(company)
    elif attribute == 'High':
        high_(company)
    elif attribute == 'Low':
        low_(company)
    elif attribute == 'Volume':
        vol_(company)
    else:
        all_(company)