import random
import pandas as pa
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as pg
diceResult=[]
df=pa.read_csv("C:\Users\Ezra\Desktop\Python\py\StudentsPerformance.csv")

mean=sum(diceResult)//len(diceResult)
print("The Mean is", mean)
median=statistics.median(diceResult)
print("The Median is", median)
mode=statistics.mode(diceResult)
print("The mode is", mode)
standard_deviation=statistics.stdev(diceResult)
print("The Stdve is", standard_deviation)
st1_start,st1_end=mean-standard_deviation,mean+standard_deviation
st2_start,st2_end=mean-2*standard_deviation,mean+2*standard_deviation
st3_start,st3_end=mean-3*standard_deviation,mean+3*standard_deviation
fig=ff.create_distplot([diceResult],["result"],show_hist=False)
fig.add_trace(pg.Scatter(mode="lines",x=[mean,mean],y=[0,0.17],name="Mean"))
fig.add_trace(pg.Scatter(mode="lines",x=[st1_start,st1_start],y=[0,0.17],name="Stdev1 Start"))
fig.add_trace(pg.Scatter(mode="lines",x=[st1_end,st1_end],y=[0,0.17],name="Stdev1 End"))
fig.add_trace(pg.Scatter(mode="lines",x=[st2_start,st2_start],y=[0,0.17],name="Stdev2 Start"))
fig.add_trace(pg.Scatter(mode="lines",x=[st2_end,st2_end],y=[0,0.17],name="Stdev2 End"))
print(count,diceResult)
fig.show()
st1_list=[result for result in diceResult if result > st1_start and result <st1_end]
print(st1_list)
st1_percentage=len(st1_list)*100/len(diceResult)
print("The Standard Deviation1 percentage is ",st1_percentage)
st2_list=[result for result in diceResult if result > st2_start and result <st2_end]
print(st2_list)
st2_percentage=len(st2_list)*100/len(diceResult)
print("The Standard Deviation2 percentage is ",st2_percentage)