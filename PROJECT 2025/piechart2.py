
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'Bitcoin SV 2.csv'
bitcoin_data = pd.read_csv(file_path)

# Aggregate the total 'High' and 'Low' values
high_low = bitcoin_data[['High', 'Low']].sum()
high = high_low['High']
low = high_low['Low']

# Create an interactive pie chart
category_data = ['High', 'Low']
value_data = [high, low]
colors = ['blue', 'orange']  # Define colors

# Show the chart
plt.pie(value_data, labels=category_data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Interactive Pie Chart from CSV Data")
plt.axis('equal')

plt.show()
