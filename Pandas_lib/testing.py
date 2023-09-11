import pandas as pd

def test():
    start_date = '2018-01-01'
    end_date = '2018-01-31'
    dates=pd.date_range(start_date,end_date)
    df = pd.DataFrame(index=dates) # create empty dataframe, index is dates
    

if __name__ == '__main__':
    test()