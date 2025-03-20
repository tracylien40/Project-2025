import pandas as pd
import plotly.express as px
import plotly.offline as pyo


file_path = 'Bitcoin SV 2.csv'  
data = pd.read_csv(file_path)


print(data.columns)

# This creates a line graph with multiple lines
fig = px.line(data, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Bitcoin Price Over Time')

# the graph as an interactive HTML file
pyo.plot(fig, filename='plotly_chart.html', auto_open=False)
