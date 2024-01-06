import pandas as pd
import matplotlib.pyplot as plt

# Load data from the CSV file
file_path = 'data/AMZN.csv'  # Replace 'your_stock_data.csv' with your file name or path
data = pd.read_csv(file_path)

# Convert the 'Date' column to a datetime object
data['Date'] = pd.to_datetime(data['Date'])

# Print the length of the data
data_length = len(data)
print("Length of data:", data_length)
print(data)

close_values = data['Close'].values

print(close_values[1])

def difference_price(t) -> float: 
    """
    Calculates difference in price for stocks between t 
    """
    return close_values[t] - close_values[t-1]

def raw_return(t) -> float: 
    """
    
    """
    return (close_values[t] - close_values[t-1]) / (close_values[t-1])*100

t = 20

print(f"Difference on stock price for {t} is {difference_price(t)} between {data['Date'].values[t]} and {data['Date'].values[t-1]}")
print(f"Raw return on stock price for {t} is {raw_return(t)} between {data['Date'].values[t]} and {data['Date'].values[t-1]}")


def log_returns() -> []:
    """
    Hello
    """

# Plotting
#plt.figure(figsize=(10, 6))
#plt.plot(data['Date'], data['Volume'], label='Close Price')
#plt.plot(data['Date'], close_values, label='Close Price')
#plt.title('Stock Close Price Over Time')
#plt.xlabel('Date')
#plt.ylabel('Price')
#plt.legend()
#plt.grid(True)
#plt.show()
