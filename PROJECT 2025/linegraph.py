import pandas as pd
import plotly.express as px


file_path = 'Bitcoin SV 2.csv'  
data = pd.read_csv(file_path)

#Before line graph is shown , the types of colums of data are shown
print(data.columns)

# My x and y axis for the dates and opening price of bitcoin data 
x_Dates ='Date'  
y_Open  = 'Open' 


# Coding Multiple lines of data on the y-axis
fig = px.line(data, x='Date', y=['Open', 'High', 'Low', 'Close'], title='Multiple Lines: Stock Data')


# Show the graph
fig.show()


