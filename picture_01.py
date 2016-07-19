from bokeh.charts import Dot, Scatter, Histogram, output_file, show
from bokeh.plotting import figure, show, output_file
from bokeh.io import push_notebook
from bokeh.models import SingleIntervalTicker, LinearAxis
#from bokeh.sampledata.autompg import autompg as df
import pandas as pd
import numpy as np

df = pd.read_csv("https://sites.google.com/site/gungorozer/data-science/euro2016_tweets.bytime")

#print df['Ronaldo']

#Minutes_After_Kickoff,Total_by_Time,Portugal,France,Ronaldo,Griezmann,Eder,Goal,Post
#df.sort('Ronaldo', inplace=True)

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


#plot = figure(width=1200, height=600)
#plot.rect(x=df['Minutes_After_Kickoff'], y=df['Ronaldo'], width=10, height=df['Ronaldo'], color="black",
#    width_units="screen", height_units="screen")

#hist = Scatter(df,x='Minutes_After_Kickoff',y=['Ronaldo','Griezmann'], 
#               title="Identifying important events", legend='top_right')
# hist = Histogram(df, values='Ronaldo', color='black',
#title="Identifying important events", legend='top_right')

output_file("important_events.html", title="Important_events.py")

show(plot)
