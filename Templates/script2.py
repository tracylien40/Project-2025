import pandas as pd
import plotly.express as px
import plotly.offline as pyo

# Load CSV Data (Make sure the file exists in the same folder)
file_path = 'Bitcoin SV 2.csv'  
data = pd.read_csv(file_path)

    
print(data.columns)  # Show available columns

    # Change these column names based on your CSV file
    
category_high = 'High'  
value_low= 'Low'  

    # Create interactive pie chart
fig = px.pie(data, names=category_high, values=value_low, title="Bitcoin Data Pie Chart")

    # Save as an HTML file and open in browser
pyo.plot(fig, filename='bitcoin_pie_chart.html', auto_open=True)

