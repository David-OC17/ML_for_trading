import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#to avoid repetition of code, we can import the daily_returns.py file and use the functions defined there
import daily_returns as dr

def test_run():
    # Read data
    dates = pd.date_range('2009-01-01', '2012-12-31')  # one month only
    symbols = ['SPY','XOM', 'GLD']
    df = dr.get_data(symbols, dates)
    dr.plot_data(df)

    # Compute daily returns
    daily_returns = dr.compute_daily_returns(df)
    
    # Check for NaN values
    if daily_returns.isnull().values.any():
        daily_returns = daily_returns.dropna()
    
    # Compute beta coefficient
    beta_XOM, alpha_XOM = np.polyfit(daily_returns['SPY'], daily_returns['XOM'], 1)
    beta_GLD, alpha_GLD = np.polyfit(daily_returns['SPY'], daily_returns['GLD'], 1)
    # Print the values of beta and alpha for XOM and GLD stocks compared to SPY
    print("beta_XOM= ", beta_XOM)
    print("alpha_XOM= ", alpha_XOM)
    
    print("beta_GLD= ", beta_GLD)
    print("alpha_GLD= ", alpha_GLD)
    
    # Plot the values of beta and alpha for XOM and GLD stocks compared to SPY
        # Error: ValueError: Multi-dimensional indexing (e.g. `obj[:, None]`) is no longer supported. Convert to a numpy array before indexing instead.
        # Solution: use np.array() to convert the pandas dataframe to numpy array
    daily_returns.plot(kind='scatter', x='SPY', y='XOM')
    plt.plot(np.array(daily_returns['SPY']), np.array(beta_XOM*daily_returns['SPY'] + alpha_XOM), '-', color='r')
    plt.show()
    
    daily_returns.plot(kind='scatter', x='SPY', y='GLD')
    plt.plot(np.array(daily_returns['SPY']), np.array(beta_GLD*daily_returns['SPY'] + alpha_GLD), '-', color='g')
    plt.show()
    
    


if __name__ == "__main__":
    test_run()
