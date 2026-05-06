import numpy as np
import pandas as pd
from pandas import Series, DataFrame

"""
Introduction to pandas Data structures:
we cover:
Series and DataFrame.
"""
# #----------------------------------------
# # SERIES
# # A Series is a one-dimensional array-like object containing a sequence of values
# # of the same types and an associated array of data labels, called its index.
# #----------------------------------------

# # The simplest Series is fromed from only an array of data:
# obj = pd.Series([4, 7, -5, 3])
# # print(obj)

# # I can insert the index within index parameter.
# obj2 = pd.Series([4, 7, -5, 3], index=["a", "b", "c", "d"])
# # print(obj2.index)

# # # I can use the lebels in the index to select single values or a set of values.
# # print(obj2['b']) # to select single value
# # print(obj2[['b', 'c', 'a']]) # to select the set of values.

# # While Using NumPy functions or NumPy-like operations, suh as filtering with a 
# # Boolean array, scalar multiplication, or applying math functions, will preserve
# # the index-vlaues(means no effect on index)
# # print(obj2[obj2 > 0]) # Boolean array.
# # print(obj2 * 2) # math functions.
# # print(np.exp(obj2)) # doint the exponent with np.exp function.

# # print("b" in obj2) # Out -> True
# # print("e" in obj2) # Out -> False.

# # Create a Series of Python dictionaries.
# sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
# obj3 = pd.Series(sdata) # The Key will become the Indices , along with the values , of dictionaries.
# print(obj3)

# # Reversing: I can aslo create a dictionary with the series.
# dic = obj3.to_dict()
# print(dic) # now the series becomes the dic.

# # I can pass the keys of the dictionaries as index, which i want to present in the series.
# state = ["California", "Ohio", "Oregon", "Texas"]
# obj4 = pd.Series(sdata, index=state)
# print(obj4) # The value of 'California' Is Nan, it's because the california
#             # doesn't have any value , Nan (Not a number) represents the value is missing, or NA or null.

# # To detect the missing data, I can use "isna" or "notna" functions.
# print(pd.isna(obj4)) # Where value is Nan or missing it will give True.

# # Series also has this as instance methods:
# print(obj4.isna())

# # A useful Series feature for many applications is tha it automatically alignn by index label in Arithmetic Operations.
# print(obj3 + obj4) # it aligned as Full outer joins, in DATABASES.

# obj4.name = "population"
# obj4.index.name = "state"
# print(obj4)

# # A Series's index can be altered in place by assignment.
# print(obj)
# obj.index = ["Bob", "Steve", "Jeff", "Ryan"]
# print(obj)

"""
DATAFRAM:
There are many ways to construct a DataFrame, though one of the most common is from
dictionary of equal_length list or NumPy arrays:
"""
# data = {
#     "State" : ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada", "Texas", "Texas"],
#     "year" : [2000, 2001, 2002, 2003, 2001, 2003, 2002, 2003],
#     "pop" : [1.5, 1.7, 3.6, 2.4, 2.9, 3.2, 3.4, 1.6],
# }

# frame = pd.DataFrame(data=data)
# # print(frame)

# # # For large data frame, head method Selects the first 5 rows:
# # print(frame.head())

# # # Similarly, tail returns the last five rows:
# # print(frame.tail())

# # # I Can arrange the dataFrame columns in any order I want.
# # print(pd.DataFrame(data, columns=["year", "State", "pop"]))

# # # If i pass columns that isn't in the dictionary, it will appear with missing values.
# frame2 = pd.DataFrame(data, columns=["year", "State", "pop", "debt"])

# # # A column in DF can be retrieved as a Series either by dict-like notation or by (.) dot notation.
# # print(frame['State'])
# # print(frame.year)

# # We can retrieve rows via , loc and iloc attributes.
# # print(frame.loc[1])
# # print(frame.iloc[2])

# # # Columns can be modified by assignment. for e.g. the empty debt column 
# # # could be assigned a scalar value or an array of values.

# # values = np.arange(25, 33)
# # frame2['debt'] = values
# # print(frame2)
# # frame2['debt'] = 25
# # print(frame2)

# # # Adding a column of Boolean values where the state column equals 'Ohio':
# # frame2['easter'] = frame2["State"] == "Ohio"
# # print(frame2)

# # # the del method can then be used to remove this column:
# # del frame2['easter']
# # print(frame2.columns)

# # Another common form of data is a nested dictionary of dictionaries:
# populations = {
#     "Ohio" : {
#         2000 : 1.5,
#         2001 : 1.7,
#         2002 : 3.6,
#     },
#     "Nevada" : {
#         2001 : 2.4,
#         2002 : 2.9,
#     }
# }

# frame3 = pd.DataFrame(populations)
# # print(frame3)

# # # I can Transpose the DataFrame with similar syntax to a NumPy array:
# # print(frame3.T)

# # Dictionaries of Series are treated in much the same way:
# pdata = {
#     "Ohio" : frame3["Ohio"][: -1],
#     "Nevada" : frame3["Nevada"][: 2],
# }
# print(pd.DataFrame(pdata))

# # DataFrame's index and columns have their name attributes set, these will also be displayed:
# frame3.index.name = "year"
# frame3.columns.name = "state"
# print(frame3)

# # DataFrame's to_numpy method returns the data contained in the DataFrame as 2D ndarray.
# print(frame3.to_numpy())

"""
Index Objects:
"""
# obj = pd.Series(np.arange(3), index=["a", "b", "c"])
# print(obj)
# index = obj.index
# print(index)

# # Index objects are immutable and thus can't be modified by
# # any operation that would modify the values or the size of the index.
# # index[0] = "d" # Out -> TypeError: Index does not support mutable operations
# # Immutability makes it safer to share index objects among data structures.
# labels = pd.Index(np.arange(3))
# print(labels)

# obj2 = pd.Series([1.5, -2.5, 0], index=labels)
# print(obj2)

# # Some users will not often take advantage of the capabilities Provided by an Index,
# # but because some operations will yield results containing indexed data, it's
# # important to understand how they work.
# populations = {
#     "Ohio" : {
#         2000 : 1.5,
#         2001 : 1.7,
#         2002 : 3.6,
#     },
#     "Nevada" : {
#         2001 : 2.4,
#         2002 : 2.9,
#     }
# }
# frame3 = pd.DataFrame(populations)
# # print(frame3)
# frame3.index.name = "year"
# frame3.columns.name = "state"
# print(frame3)
# print(frame3.columns)

"""
Essential Functionality:
"""
# ---------------------------------
# Reindexing
# ---------------------------------

# An important method on pandas objects is reindex, Which means to create a new
# object with the values rearranged to align with the new index. 

# # let's take an example
# obj = pd.Series([4.5, 7.2, -5.3, 3.6], index=["d", "b", "a", "c"])
# print(obj)

# # calling reindex on this Series rearranges thedata according to the new index,
# # introducing missing values if any index values were no already present:
# obj2 = obj.reindex(["a", "b", "c", "d", "e"]) # Since e is not the previous obj , it'll be Nan
# print(obj2)

# # For ordered data like time series, we may want to do some interpolation, 
# # or filling of vlaues when reindexing. The method option allows us to do this,
# # using a method such as ffill, which forward-fills the values:
# obj3 = pd.Series(["Blue", "Green", "Yellow", "Pink"], index=[0, 2, 4, 6])
# print(obj3)

# new_obj = obj3.reindex(np.arange(8), method="ffill") # forward fill the values.
# print(new_obj)

# With DataFrame, reindex can alter the (row) index, columns, or both. When passed
# only a sequence, it reidexes the rows in the result:
# frame = pd.DataFrame(np.arange(9).reshape((3,3)), index=["a", "c", "d"], columns=["Ohio", "Texas", "California"])
# print(frame)

# print(frame.reindex(["a", "b", "c", "d"]))
# print(frame.reindex(columns=["Texas", "Utah", "California"]))

# # well I can do this with the help of loc and iloc method as well:
# print(frame.loc[["a", "c", "d"], ["Texas", "California"]])

"""
Dropping Entries from an Axis
"""
# obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
# print(obj)

# new_obj = obj.drop("c") # It'll produce a new object without the rown "c".
# print(new_obj)  
# print(obj.drop(["d", "c"])) # I can use python list or arrays for it.

# data = pd.DataFrame(np.arange(16).reshape((4, 4)),
#                     index= ["Ohio", "Colorado", "Utah", "New York"],
#                     columns= ["one", "two", "three", "four"]
#                     )
# print(data)
# print(data.drop(index=["Colorado", "Ohio"]))
# print(data.drop(columns=["two", "four"]))

# # to drop values from the columns by passing axis=1 (which is like NumPy) or axis = "columns".
# print(data.drop("two", axis=1))

# print(data.drop(["two", "three"], axis="columns"))

"""
Indexing, Selection, and Filtering:
"""

obj = pd.Series(np.arange(4.), index=["a", "b", "c", "d"])
print(obj)
print(obj["b"])
print(obj[2:4])
print(obj.loc[["b", "c", "a"]])
print(obj.iloc[[1,3]])
print(obj[obj < 2]) # Boolean array indexing.

data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"],
                    )

print(data)