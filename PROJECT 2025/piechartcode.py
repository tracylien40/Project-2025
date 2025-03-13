
import pandas as pd
import matplotlib.pyplot as plt
# My dataset
file_path = 'Bitcoin SV 2.csv'
bitcoin_data = pd.read_csv(file_path)

# the total 'High' price  and 'Low' price values
high_low = bitcoin_data[['High', 'Low']].sum()
high = high_low['High']
low = high_low['Low']

# Interactive pie chart 
category_data = ['High', 'Low']
value_data = [high, low]
colors = ['green', 'red']  # Colours

# To produce the chart
plt.pie(value_data, labels=category_data, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Interactive Pie Chart using Bitcoin Data")
plt.axis('equal')

plt.show()
