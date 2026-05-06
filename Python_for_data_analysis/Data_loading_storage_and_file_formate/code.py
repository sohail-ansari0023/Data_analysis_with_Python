import pandas as pd
import numpy as np


"""
    read_csv() method.
"""

# df = pd.read_csv('examples/ex1.csv')
# print(df)

# To add specific column names , Use name attribute, inside the read_csv() function.

df = pd.read_csv('examples/ex1.csv', names=["hello", "hhi", 'you', "fine", "now"])

print(df)
