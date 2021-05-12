import random
import scipy
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
count=[]
dataSet=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dataSet.append(dice1+dice2)
    count.append(i)
fig=ff.create_distplot([dataSet],["result"],show_hist=False)
mean=statistics.mean(dataSet)
median=statistics.median(dataSet)
mode=statistics.mode(dataSet)
standardDeviation=statistics.stdev(dataSet) 
FirstStandardDeviationStart,FirstStandardDeviationEnd=mean-standardDeviation,mean+standardDeviation
SecondStandardDeviationStart,SecondStandardDeviationEnd=mean-2*standardDeviation,mean+2*standardDeviation
ThirdStandardDeviationStart,ThirdStandardDeviationEnd=mean-standardDeviation*3,mean+standardDeviation*3
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))
fig.add_trace(go.Scatter(x=[FirstStandardDeviationStart,FirstStandardDeviationStart],y=[0,0.17],mode="lines",name="FSDS"))
fig.add_trace(go.Scatter(x=[FirstStandardDeviationEnd,FirstStandardDeviationEnd],y=[0,0.17],mode="lines",name="FSDE"))
fig.add_trace(go.Scatter(x=[SecondStandardDeviationStart,SecondStandardDeviationStart],y=[0,0.17],mode="lines",name="SSDS"))
fig.add_trace(go.Scatter(x=[SecondStandardDeviationEnd,SecondStandardDeviationEnd],y=[0,0.17],mode="lines",name="SSDE"))
fig.add_trace(go.Scatter(x=[ThirdStandardDeviationStart,ThirdStandardDeviationStart],y=[0,0.17],mode="lines",name="TSDS"))
fig.add_trace(go.Scatter(x=[ThirdStandardDeviationEnd,ThirdStandardDeviationEnd],y=[0,0.17],mode="lines",name="TSDE"))
fig.show()
listOfFirstSD=[result for result in dataSet if result>FirstStandardDeviationStart and result<FirstStandardDeviationEnd]
listOfSecondSD=[result for result in dataSet if result>SecondStandardDeviationStart and result<SecondStandardDeviationEnd]
listOfThirdSD=[result for result in dataSet if result>ThirdStandardDeviationStart and result<ThirdStandardDeviationEnd]
print("Mean: ",mean)
print("Median: ",median)
print("Mode: ",mode)
print("SD: ",standardDeviation)
print("list of first SD:",(len(listOfFirstSD)*100.0/len(dataSet)))
print("list of second SD:",(len(listOfSecondSD)*100.0/len(dataSet)))
print("list of third SD:",(len(listOfThirdSD)*100.0/len(dataSet)))