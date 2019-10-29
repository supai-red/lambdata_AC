"""
utility functions for working with dataframes
"""
import pandas as pd
import numpy as np
from random import randint 

def list_series_df(a_list):
  """A function to turn a list, into a series, and then a DataFrame.."""
  s = pd.Series(a_list)
  df = pd.DataFrame(s)
  print("The DataFrame is")
  return df  

def check_nulls(df):
    """A function to check for and print DataFrame nulls."""
    print(df.isnull().sum().sum())
    return 

def year_month(df, col_with_dt):
  """A function to extract year and month form Pandas datetime format"""
  year_only = df['date_time'].dt.year
  month_only = df['date_time'].dt.month
  df['year_only'] = year_only 
  df['month_only'] = month_only
  return df