import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

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

# Calculate Sharpe Ratio for a portfolio (monthly)
def sharpe_ratio(portfolio, risk_free_rate = 0.0, K=12):
    """
    portfolio: pandas dataframe with monthly returns for each stock
    risk_free_rate: risk free rate of return (default: 0.0)
    """
    # Calculate excess return over risk free rate
    excess_return = portfolio - risk_free_rate
    
    # Calculate average excess return
    avg_excess_return = excess_return.mean()
    
    # Calculate standard deviation of excess return
    std_excess_return = excess_return.std()
    
    # Calculate Sharpe Ratio
    sharpe_ratio = np.sqrt(K) * avg_excess_return/std_excess_return
    
    return sharpe_ratio

# Used to introduce error in the polynomial fit
    # Done in order to avoid overfitting 
def error_poly(C, data):
    err = np.sum((data[:, 1] - np.polyval(C, data[:, 0])) ** 2)
    return err

def fit_poly(data, error_poly=error_poly,degree=3):
    # Generate initial guess for polynomial model (all coeffs = 1)
    Cguess = np.poly1d(np.ones(degree + 1, dtype=np.float32))

    # Call optimizer to minimize error function
    result = opt.minimize(error_poly, Cguess, args=(data,), method='SLSQP', options={'disp': True})
    
    return np.poly1d(result.x)
    
def predict_portfolio(polynomial, start_date, end_date):
    dates = pd.date_range(start_date, end_date)
    return np.polyval(polynomial, dates)
    
def fill_missing_values(df):
    df.fillna(method='bfill', inplace=True)
    df.fillna(method='ffill', inplace=True)
    return df

def predict_sharpe_ratio(polynomial, start_date, end_date, risk_free_rate = 0.0):
    dates = pd.date_range(start_date, end_date)
    portfolio = pd.DataFrame(index=dates)
    portfolio['portfolio'] = np.polyval(polynomial, dates)
    return sharpe_ratio(portfolio, risk_free_rate)

def main():
    symbols = ['GOOG', 'AMZN', 'SPY', 'GLD']
    dates = pd.date_range('2010-01-01', '2010-12-31')
    past_dates = pd.date_range('2009-01-01', '2009-12-31')
    risk_free_rate = 10.0/100/12 # monthly risk free rate of return (CETES)
    K = 12 # number of periods per year
    
    df_past = get_data(symbols, past_dates)
    df = get_data(symbols, dates)
    
    df = df/df.iloc[0,:]
    df_past = df_past/df_past.iloc[0,:]
    df = fill_missing_values(df)
    df_past = fill_missing_values(df_past)
    
    # Predict the sharpe ratio month by month for 2010
    for i in range(12):
        start_date = '2010-{}-01'.format(i+1)
        end_date = '2010-{}-01'.format(i+2)
        polynomial = fit_poly(df_past, error_poly, 3)
        sharpe_ratio = predict_sharpe_ratio(polynomial, start_date, end_date, risk_free_rate)
        print("Sharpe ratio for {} is {}".format(start_date, sharpe_ratio))
        
        # Add this month's data to the past data
        df_past = df_past.append(df.loc[start_date:end_date])
        
    

if __name__ == "__main__":
    main()