import pandas as pd
import numpy as np


# Load the csv_file.
df = pd.read_csv('messy_registry_data.csv')

# 1. Get an overview of the data.
# print(df.info())

# 2. Let's see if data contains any Missing values.
# print(df.isna().sum())
"""
what is happining here?

df.isna() goes through our entire dataset and returns True if a cell is missing
and Flase if it has data.
   
.sum() addd up all the True Values (since True = 1) column by column. This gives us
'a clear report card of our missing data.
"""

# 3. Dropping any row witha missing value, (dropna())
df_clean = df.dropna()
print(df_clean.info())
print(df_clean.isna().sum())
print(df_clean[['Carrier_ID', 'Company Name', 'Registration_Date', 'Fleet_Size', 'Contact_Number', 'HQ_Location']])