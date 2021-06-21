import plotly.graph_objects as go
from plotly.offline import plot
from file_reader import create_DataFrame
#df_TechMahindra = create_DataFrame('TECHM')
def interactive_graph(company,name):
    fig = go.Figure(
    data = go.Ohlc(
        x = company.index,
        open = company['Open'],
        high = company['High'],
        low = company['Low'],
        close = company['Close'],
        increasing_line_color = 'green',
        decreasing_line_color = 'red',
        ))
    fig.update_layout(
    title = name
    )
    plot(fig,show_link = True, filename = name+'.html')
