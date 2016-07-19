from bokeh.charts import Dot, Scatter, Histogram, output_file, show
from bokeh.plotting import figure, show, output_file
from bokeh.io import push_notebook
from bokeh.models import SingleIntervalTicker, LinearAxis
import pandas as pd
import numpy as np

df = pd.read_csv("https://sites.google.com/site/gungorozer/data-science/euro2016_tweets.bytime")


plot = Dot(df,values='Ronaldo', label='Minutes_After_Kickoff',
           title="Python Interpreter Sampling",
           legend=None, tools=None, width=1200)
plot.axis.visible = None
ticker = SingleIntervalTicker(interval=5, num_minor_ticks=10)
xaxis = LinearAxis(ticker=ticker)
ticker = SingleIntervalTicker(interval=200, num_minor_ticks=400)
yaxis = LinearAxis(ticker=ticker)
plot.add_layout(xaxis, 'below')
plot.add_layout(yaxis, 'left')
plot.xaxis.axis_label = 'Minutes after kickoff'
plot.yaxis.axis_label = 'Count of Ronaldo words'

output_file("important_events.html", title="Important_events.py")

show(plot)
