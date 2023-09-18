# Portfolio optimizer

This is a mini-project for the course, where an optimizer for a portfolio that invests into 4 stocks is built.

This said optimzier if built to maximize the Sharpe Ratio of the portfolio, by looking at a polynomial regression of past activity and computing the ratio from the predictions for the future.

## Details

* Since it is only logical to allocate 100% of the portfolio money at any time, the optimizer is constrained so it only produces values that add up to 100%.
* In a real scenario, the optimizer would be excuted every months of so, adjusting the regression based formula and the Sharpe Ratio.
* The 4 stocks to be considered for this mini-project are SPY( SPDR S&P 500 ETF Trust), GLD (Gold), AMZN (Amazon) and GOOG (Google)

**Note:** This is optimizer is built for educational purposes only, and should not be used as a means for real investment and trading.