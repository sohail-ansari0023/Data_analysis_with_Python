import pandas as pd
import numpy as np
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df= pd.read_csv(url, header=None)

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels", "engine-location", "wheel-base",
           "length", "width", "height", "curb-weight", "engine-type", "num-of-cylinders",
           "engine-size", "fuel-system", "bore", "stroke", "compression-ration", "horsepower",
           "peak-rpm", "city-mpg", "highway-mpg", "price"]

df.columns = headers
# print(df.head(40))
#----------------------------------------
# [df.head(n)] shows the first n rows of dataframe.
# print(df.head(5))
# [df.tail(n)] shows the last n rows of dataframe. 
# print(df.tail(5))

#-----------------------------------------
# [df.describe()] Returns a statistical Summary. However the this method
# will ignore the columns who doesn't contain numbers.
# print(df.describe()) 
# [df.dtype()] will return the type of each columns.
# print(df.dtypes )

"""
The DATA Pre-Processing:
------------------------------------------------------------------------
The process of coverting or Mapping the data from the initial "Raw" format
into another format, in order to prepare the data for further analysis.
Also known as:
    - Data Cleaning, and
    - Data Wrangling

"""

# Simple data frame operation.

# Accesing each column by their name
# print(df["body-style"])

# to manipulate data.
# print(df["body-style"]+"hello")

"""
Handling the missing value:

Missing value somethin when no data value is stored for a variable 
(feature) in an observation.
It could be represented as "?", "N/A", 0 or just a blank cell.

How to deal with Missing value?


"""

# changing the type of data.
"""first check the type by df.dtypes() using the (numpy module)"""
# print(df["normalized-losses"].dtype)
# df['normalized-losses'] = pd.to_numeric(df["normalized-losses"], errors='coerce')
# print(df["normalized-losses"].dtype)
# df = df.replace("?", np.nan)
# print(df.head(40))

# How to drop missing values in Python.
"""--- Use dataframes.dropna(): 
the dropna() function have parameters like:
- axis=0 drops the entire row,
- axis= 1 drops the entire column.
 """
# clean_df = df.dropna(subset='normalized-losses')
# print(clean_df.head(40))

# How to replace missing value.

data = pd.read_fwf("data/2002FemResp.dat.gz", compression="gzip")
print(data.describe())




