import pandas as pd
import matplotlib.pyplot as plt


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)

    for symbol in symbols:
        # TODO: Read and join data for each symbol
        df_temp = pd.read_csv("../data/{}.csv".format(symbol),
                index_col = 'Date', 
                parse_dates = True,
                usecols=['Date', 'Adj Close'], 
                na_values=['nan'])
        df_temp = df_temp.rename(columns = {'Adj Close': symbol})
        df = df.join(df_temp, how = 'inner')
        
    df = df.sort_index() # sort by date (chronological order)
    return df

def main():
    # Define a date range (modify if necessary)
    dates = pd.date_range('2010-01-01', '2010-12-31')

    # Choose stock symbols to read
    symbols = ['GOOG', 'AMZN', 'SPY', 'GLD']
    
    # Get stock data
    df = get_data(symbols, dates)
    print(df)
    
    # Normalize data and fill missing values
    df = df/df.iloc[0,:]
    df.fillna(method='bfill', inplace=True)
    df.fillna(method='ffill', inplace=True)
    
    # Plot data to see the evolution of stock prices
    df.plot()
    plt.show()

if __name__ == "__main__":
    main()