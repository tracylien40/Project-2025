import pandas as pd

# The dataset
input_file = 'Bitcoin SV 2.csv'
data = pd.read_csv(input_file)

# Display initial analysis
print("First 5 rows of the dataset:")
print(data.head())

print("\nDataset Information:")
print(data.info())

# Handle missing values
data.fillna(method='ffill', inplace=True)  # Forward fill
data.fillna(method='bfill', inplace=True)  # Backward fill for additional coverage

# Remove unwanted text
data = data.replace(r"\{'waiting lists':\}", "", regex=True)

# Rename 'VALUE' column to 'Number' if it exists
if "VALUE" in data.columns:
    data.rename(columns={'VALUE': 'Number'}, inplace=True)

# Drop 'UNIT' column if it exists
if "UNIT" in data.columns:
    data.drop(columns=["UNIT"], inplace=True)

# Process non-numerical data: convert categorical columns to numerical if needed
for col in data.select_dtypes(include=['object']).columns:
    data[col] = data[col].astype(str).str.strip()  # Remove unwanted spaces
    if data[col].nunique() < 10:  # Encode if few unique values
        data[col] = data[col].astype('category').cat.codes

# numeric values
data = data.applymap(lambda x: ''.join(filter(str.isdigit, str(x))) if isinstance(x, str) else x)

# Save cleaned data
output_file = 'cleandata.csv'
data.to_csv(output_file, index=False)

print("\nData has been cleaned successfully! Saved as:", output_file)

#  Calculates the Mean of the 'High' price 
if 'High' in data.columns:
    # the 'High' column to numeric type
    data['High'] = pd.to_numeric(data['High'], errors='coerce')
    
    mean_high = data['High'].mean()
    print(f"\nMean of High column: {mean_high}")
else:
    print("\nColumn 'High' not found in the dataset.")
