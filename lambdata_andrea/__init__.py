"""
lambdata - a collection of data science helper functions
"""

import pandas as pd 
import numpy as np 

def check_nulls(df):
    """A function to check for and print DataFrame nulls."""
    print(df.isnull().sum().sum())
    return 

def list_series_df(a_list):
  """A function to turn a list, into a series, and then a DataFrame.."""
  s = pd.Series(a_list)
  df = pd.DataFrame(s)
  print("The DataFrame is")
  return df     