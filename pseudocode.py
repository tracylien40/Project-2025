Step 1: Import Libraries and Load Data
Import the libraries needed (pandas, matplotlib, plotly.express).
Load the dataset Bitcoin SV 2.csv using pandas.read_csv().

Step 2: Data Inspection
Display the rows of the dataset.
Show the dataset information to understand its structure (in a column).

Step 3: Handle Missing Data
Fill missing values using forward fill (fillna(method='ffill')).
Apply backward fill (fillna(method='bfill')) for extra coverage.

Step 4: Data Cleaning
Replace unwanted text ({'waiting lists':}) using regex.
If the column “VALUE” exists, rename it to “Close” for clarity.
Drop the “UNIT” column if it exists.

Step 5: Handle Categorical Data
Loop through each column in the dataset:
For categorical columns (non-numerical), clean by stripping spaces and encoding values as categories if they have fewer than 10 unique values.

Step 6: Remove Non-Numeric Characters
Apply a transformation to remove non-numeric characters from all cells in the dataset.

Step 7: Save Cleaned Data
Save the cleaned dataset into a new file cleandata.csv.

Step 8: Data Visualization (Pie Chart using matplotlib)
Read the cleaned dataset.
Calculate the total ‘High’ and ‘Low’ price values from the dataset.
Create an interactive pie chart showing the proportions of ‘High’ and ‘Low’ values.
Show the pie chart using matplotlib.

Step 9: Data Visualization (Line Chart using plotly)
Read the cleaned dataset again.
Make a line graph to show Bitcoin’s price over time for ‘Open’, ‘High’, ‘Low’, and ‘Close’ values.
Save this chart as an interactive HTML file (plotly_chart.html).

Step 10: HTML Structure for Crypto Dashboard
Create an HTML structure with a sidebar for navigation and a content area for displaying Bitcoin-related information (cards for price info, embedded interactive charts).
Use <iframe> to embed the Plotly chart (plotly_chart.html) in the dashboard.
Add navigation buttons like “About” and “Trade” to the sidebar.

Step 11: Create “About” Page
Create an About page explaining Bitcoin and its price changes.
Add an embedded interactive pie chart displaying Bitcoin price distribution.
Add a “Back to Dashboard” button to navigate back to the main dashboard.

Step 12: Add “Back” Navigation Button
Ensure a navigation experience by adding a “Back to Dashboard” button in both the dashboard and “About” pages to switch between them.

