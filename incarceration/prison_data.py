#imports
#plotly.offline and graph objects for graphs
#pandas for data 
import plotly.offline as pyo 
import plotly.graph_objects as go
import pandas as pd

#creating pandas dataframes
df = pd.read_excel(r'/Users/personal/Desktop/incarceration/prisoners.xlsx')
df2 = pd.read_excel(r'/Users/personal/Desktop/incarceration/prisoners2.xlsx')

#Line Plot
trace1 = go.Line(
    x = df['Year'],
    y = df['U.S. Total'],
    mode = 'markers+lines',
    name = 'Inmates'    
)
#Transparent box data
trace2 = go.Scatter(
    x=df['Year'],
    y=['U.S. Total'],
    mode="lines",
    name="Reagan's Presidency"
)

#Setting data using traces
data = [trace1, trace2]

#Creation of layout - styling for graph
layout = go.Layout(
    title = 'Incarcerated Americans in the United States from 1955 to 1994',
    xaxis_title = 'Year',
    yaxis_title = 'Incarcerated Individuals (Millions)',
    
    
)
#defining figure with data and layout
fig = go.Figure(data=data,layout=layout)

#Transparent box highlighting Reagan's years in office - addition to layout
fig.update_layout(
    shapes=[
        # 1st highlight during Feb 4 - Feb 6
        dict(
            type="rect",
            # x-reference is assigned to the x-values
            xref="x",
            # y-reference is assigned to the plot paper [0,1]
            yref="paper",
            x0="1981",
            y0=0,
            x1="1989",
            y1=1,
            fillcolor="LightSalmon",
            opacity=0.5,
            layer="below",
            line_width=0
        )  
    ]
)

#plotting figure in an html file
pyo.plot(fig, filename='reagan.html')


