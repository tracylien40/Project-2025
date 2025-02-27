import pandas as pd

# The dataset
input_file = 'Bitcoin SV 2.csv'
data = pd.read_csv(input_file)

# Used for the initial analysis
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

# Missing values
data.fillna(method='ffill', inplace=True)  # Forward fill missing values
data.fillna(method='bfill', inplace=True)  # Backward fill for additional coverage

# Remove unwanted text (e.g., "{'waiting lists':}")
data = data.replace(r"\{'waiting lists':\}", "", regex=True)

#Renaming the data cloumns since it represents the closing price 
if "VALUE" in data.columns:
    data.rename(columns={'VALUE': 'Close'}, inplace=True)

# Drop 'UNIT' column if it exists
if "UNIT" in data.columns:
    data.drop(columns=["UNIT"], inplace=True)

# Processing no numberical data  Convert categorical columns to numerical 
for col in data.select_dtypes(include=['object']).columns:
    data[col] = data[col].astype(str).str.strip()  # Remove unwanted spaces
    if data[col].nunique() < 10:  # Encode if few unique values
        data[col] = data[col].astype('category').cat.codes

# Taking out numerical values 
data = data.applymap(lambda x: ''.join(filter(str.isdigit, str(x))) if isinstance(x, str) else x)

# Saving my cleaned data as cleandata.csv
output_file = 'cleandata.csv'
data.to_csv(output_file, index=False)

print("\nData has been cleaned successfully! Saved as:", output_file)
