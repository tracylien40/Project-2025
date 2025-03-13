import statistics
import pandas


# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('crypto_data.csv')


# Filter out the column, value_eur
Use_BTC = df['Use_BTC'] 
print(Use_BTC)
Use_BTC = df['Use_BTC']
print(Use_BTC)


Use_ETH = df['Use_ETH']
print(Use_ETH)
Use_ETH= df['Use_ETH']
print(Use_ETH)

Use_USDT = df['Use_USDT']
print(Use_USDT)
Use_USDT= df['Use_USDT']
print(Use_USDT)

print(Use_BTC, Use_ETH,Use_USDT)