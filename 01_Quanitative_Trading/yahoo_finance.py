import yfinance as yf

def download_stock_data(ticker, start_date, end_date, filepath):
    # Download stock data
    stock = yf.download(ticker, start=start_date, end=end_date)
    
    # Save data to a CSV file
    stock.to_csv(filepath)

if __name__ == "__main__":
    ticker_symbol = "AMZN"  # Amazon's ticker symbol
    start_date = "2023-01-01"  # Start date for the data
    end_date = "2024-01-01"    # End date for the data
    file_path = "data/stocks/amazon_stock_data.csv"  # Filepath to save the CSV file
    
    download_stock_data(ticker_symbol, start_date, end_date, file_path)
