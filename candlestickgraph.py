from matplotlib.pyplot import tight_layout
import mplfinance as mpf
def candle_stick(company):
    mpf.plot(company, type = 'candle',figratio = (20,12), mav = (20), volume = True,tight_layout = True)
