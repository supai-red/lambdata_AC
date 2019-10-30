"""
utility functions for working with dataframes
"""
import pandas as pd
import numpy as np
from random import randint 

def year_month(df, col_with_dt):
  """A function to extract year and month form Pandas datetime format"""
  year_only = df['date_time'].dt.year
  month_only = df['date_time'].dt.month
  df['year_only'] = year_only 
  df['month_only'] = month_only
  return df
  