# General notes

## Pandas library
General sintax and functions to know.
```python
import pandas as pd

df = pd.DataFrame(...)
df[10:21] #slicing, end not inclusive
df['Column'].max() #max value
df['Column'].mean() #mean value
df = df.join(df2) #left join for two df
df = pd.read_csv("file.csv",
                index_col = 'Date', #use 'Date' as index
                parse_dates = True, #make them date-time index objetcs
                usecols=['Date', 'Adj Close'], #specify columns to use
                na_values=['nan']) #specify sintax of Nan values
df = df.dropna() #drop all Nan values
df.join(df2, how='inner') #

#Read in more stocks
symbols = ['GOOG', 'IBM', 'GLD'] #Google, IBM and gold
for symbol in symbols:
    df_temp = pd.read_csv('data/{}.csv'.format(symbol), ...) #format for different files
    df_temp = df_temp.rename(columns = {'Adj Close': symbol}) #change column name to avoid overlad
    df = df.join(df_temp) #left join

```

* join:
    how{‘left’, ‘right’, ‘outer’, ‘inner’, ‘cross’}, default ‘left’

            - left: use calling frame’s index (or column if on is specified)
            - right: use other’s index.
            - outer: form union of calling frame’s index (or column if on is specified) with other’s index, and sort it lexicographically.
            - inner: form intersection of calling frame’s index (or column if on is specified) with other’s index, preserving the order of the calling’s one.
            - cross: creates the cartesian product from both frames, preserves the order of the left keys.