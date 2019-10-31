# lambdata_AC
A package with data science helper functions

There are two files with DataFrame helper functions.

ds_utils.py
contains the year_month function 
which takes a Pandas DataFrame column in datetime format and returns a column with 'year only' and another with 'month only.

__init__.py
import pandas and numpy. 
There are two additional dataframe functions.

check_nulls checks and sums the nulls from a dataframe.

list_series_df turns a list, into a Pandas series, then into a Pandas DataFrame.
