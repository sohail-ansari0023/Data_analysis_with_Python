import numpy as np

"""
To get an idea of the performance difference,
consider a NumPy array of one million integers, and 
the equivalent Python list:
"""

# my_arr = np.arange(1_000_000)
# my_list = list(range(1_000_000))

# # Now let's multiply each sequence by two:
# import time
# # For Array
# start_1 = time.time()
# my_arr2 = my_arr * 2
# end_1 = time.time()
# result_1 = end_1 - start_1

# # For list
# start_2 = time.time()
# my_list2 = [x * 2 for x in my_list]
# end_2 = time.time()
# result_2 = end_2 - start_2

# print(f"Array takes {result_1} : List takes {result_2}")
# In this case the array is almost 22 times faster than the list.

"""
How Numpy enables batch computations with similar syntax to scalar values
on built-in Python objects
"""
# data = np.array([[1.5, -0.1, 3],[0, -3, 6.5]])
# print(data, end="\n"*2)

# # Writing the mathematical operations with data:
# multi_10 = data * 10 # All elements have been multiplied by 10
# print(multi_10, end="\n"*2)

# add_by_itself = data + data # each values in cells have been added to each other.
# print(add_by_itself, end="\n"*2)

# print(data.shape)
# print(data.dtype)

"""
Creating ndarrays:

The easiest way to create an array is to use the array function.
This accepts any sequence-like object (including other arrays) and
produces a new NumPy array containing the passed data.
"""
# # -- Converting a list into array.
# data1 = [2, 5, 2, 6, 8 ,0]
# arr1 = np.array(data1)
# # print(type(arr1)) # <class 'numpy.ndarray'>

# # -- A list of equal length lists, will be converted into multi-dim array.
# data2 = [[2, 5, 2, 5], [8, 7, 0, 9]]
# arr2 = np.array(data2)
# print(arr2)

# # -- To check the dimension (ndim) and to check shape of the array (shape) attribues.
# print(arr2.ndim) # out -> 2  since the arr2 has 2 dimension
# print(arr2.shape) # out -> (2, 4) arr2 has 2 rows and 3 columns.

# # -- To check the data type for the array that it creates. (dtype)
# print(arr2.dtype) # out -> int64

# -- numpy.zeros and numpy.ones create arrays of 0s or 1s.
# print(np.zeros(10)) # out -> [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# print(np.ones(10, dtype='i8')) # out -> [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# # we can provide the shape and length too.
# print(np.zeros((3, 6),)) # out -> a two dimensional array with zeroes havin 3 rows and 6 columns.
# print(np.ones_like((2, 4)))
# -- numpy.arange is an array-valued version of the built-in Python range function:
# print(np.arange(15)) # out -> [0, 1, 2, 3, 4 ,5 , ........, 14, 15]

# -- To convert or Cast an array from one data type to another we use ndarray's (astype) method.
# arr = np.array([1, 2, 4, 5, 5, 2])
# print(arr.dtype) # out -> 'int64'

# float_arr = arr.astype(np.float64)
# print(float_arr.dtype) # out -> 'float64'

# # -- I can also use another array's dtype attribute:
# int_arr = np.arange(10)
# claiber = np.array([0.22, 0.44, .33, .001], dtype=np.float64)

# print(int_arr.astype(claiber.dtype))

"""
Arithmetic with NumPy Arrays.
"""
# arr = np.array([[1., 2., 3.], [4., 5., 6.]])
# # print(arr.dtype)

# # Multipyling the array with itself.
# print(arr * arr)

# # Adding the array with itself.
# print(arr + arr)

# # Substracting the array with itself.
# print(arr - arr)  # --> we will get a Null/Zero martrics.

# # Inversing the Matrics.
# print(1 / arr)

# # Squaring the array.
# print(arr ** 2)

# # Comparisons between arrays of the same size yield Boolean arrays.
# arr2 = np.array([[0, 4, 1], [7, 2, 12]])
# print(arr > arr2)
# --> Output
# [[ True False  True]
#  [False  True False]]  BOOLEAN ARRAY.

# NOTE :- Evaluating operations between differently sized arrays are called broadcasting.

"""
BASCIC INDEXING AND SLICING.

Well, Numpy Indexing is a deep topic, we'll move to it later, first let's cover
indexing of One-Dimesional array , on the surface it is generally like the list of python.
"""
# let's build an array.
# arr = np.arange(10)
# print(arr)  # output -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(arr[5]) # Indexing. Output -> 5
# print(arr[5:8]) # Slicing. Output -> [5, 6, 7]
# arr[5:8] = 12
# print(arr)  # Output -> [0, 1, 2, 3, 4, 12, 12, 12, 8, 9]

# # NOTE An important first distinction from Python's built-in lists is that
# # array slices are views on the original array. This means that the data is not copied, and
# # any modifications to the view wil be reflected in the source array.

# # Example:
# arr_slice = arr[5:8]
# print(arr_slice)  # Output -> [12, 12, 12]

# # Now if change a vlue in arr_slice , the changes will also be reflected on original array.
# arr_slice[1] = 12345
# print(arr)

# well if I want to copy a slice of an ndarray instead of a view, you will need to
# explicitly copy the array- for example (arr[5:8].copy()), As you will see, Pandas works this
# way, too.

"""Indexing and Slicing on 2-Dimesional and Multid-imesnsional arrays."""

# 2-Dimesional Arrays.
# # let's make  and array
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr2d[2]) # Output will be a one dimensional array [7, 8, 9].

# # Thus to access individual arrays , we do it by recursive.
# print(arr2d[2][0]) # output 7.
# # To make this short we can pass a comma-separated list of indices to select
# # individual elements.
# print(arr2d[2, 0]) # output 7.

# For an illustration of indexing on a two-dimensional array. It will be helpful to
# think of axis 0 as the 'rows' and axis 1 as the 'columns'. the coordinate will be
# (axis 0 , axis 1).

# Multi-Dimesional array.
# arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# print(arr3d) # The array is in the order of (2 x 2 x 3).

# print(arr3d[1]) # give the 2-dimensional array [[7, 8, 9], [10, 11, 12]]
# print(arr3d[1, 0]) # give the one-dimensional array [7, 8, 9]
# print(arr3d[1, 0][2]) # give the individual input from the one-d array, i.e. 9

# # Both scalar values and arrays can be assigned to arr3d[0].
# old_values = arr3d[0].copy()

# arr3d[0] = 42
# print(arr3d)

# arr3d[0] = old_values
# print(arr3d)

# NOTE- The multidimensional indexing syntax for NumPy will not work with regular Python objects,
# such as lists of lists.

# my_list = [[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]]
# print(my_list[0]) # Output -> [[1, 2, 3], [4, 5, 6]]
# print(my_list[0, 1][1]) # Output -> error
# print(my_list[0][1][2]) # Output -> 6

"""
Indexing with slices.
"""

# Like one-dimensional objects such as Python list, ndarrays can be sliced with the fimiliar syntsx:
# Now consider the 2-dimensional array from befor, arr2d. slicing this array is a bit different.
# arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) # the array is in order of (3 x 3)
# print(arr2d)

# print(arr2d[: 2]) # Output -> [[1, 2, 3], [4, 5, 6]]
# # this particular method slice on axis 0, the first axis, It will read as "Select the first two rows of arr2d."

# print(arr2d[: 2][1 :]) # Output - [[2, 3], [5, 6]]

# # Select the second row but only the first tow columns.
# print(arr2d[1][: 2])
# # or
# print(arr2d[1, :2])

# NoW
# lower_dim_slice = arr2d[1, :2]
# print(lower_dim_slice.shape)

# print(arr2d[:2, 2])

# print(arr2d[:, :1])

# arr2d[:2, 1:] = 0
# print(arr2d)

# print(arr2d[2], arr2d[2].shape)
# print(arr2d[2, :], arr2d[2, :].shape)
# print(arr2d[2:, :], arr2d[2:, :].shape)

"""
BOOLEAN INDEXING
"""
# Let's take an array with some data and an array of names with duplicates.
# names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
# data = np.array([[4, 7], [0, 2], [-5, 6], [0, 0], [1, 2], [-12, -4], [3, 4]])
# print(names) # Output -> array(['Bob' 'Joe' 'Will' 'Bob' 'Will' 'Joe' 'Joe'])
# print(data)

# comparing names with the string "Bob" will return a Boolean array.
# print(names == "Bob")

# This Boolean array can be passed when indexing the array:
# data[names == "Bob"]
# print(data[names == "Bob"])

# NOTE - The length of the Boolean array and the length of the array which are indexing should be equal.

# Select from the rows where names == "Bob" and index the columns, too:
# print(data[names == "Bob", 1:])

# To Select everything but "Bob" we use either != operator or "~" symbol:
# print(names != "Bob")
# print(~(names == "Bob"))

# print(data[~(names == "Bob")])

# multiple Boolean conditios, use Boolean arithmetic operators like & (and) and | (or):

# mask = (names == "Bob") | (names == "Will")
# print(mask)
# print(data[mask])

# NOTE - The Python keywords and and or do not work with Boolean arrays. Use & (and) and | (or) instead.

# print(data < 0) # gives us a Boolean matrix.
# now let's substitute all the negative number to zero using the following comparison.
# data[data < 0] = 0
# print(data)

# we can also set the whole columns or rows using a one-dimensional Boolean array.
# data[names != "Joe"] = 7
# print(data)

"""
Fancy Indexing:
Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays.
"""
# Suppose we have an 8 X 4 array:
# arr = np.zeros((8, 4))
# # print(arr)

# for i in range(8):
#     arr[i] = i

# print(arr)

# # To select a subset of the rows in a particular order, simply pass a list or ndarray of integers
# # specifying the desired order:

# # Suppose from the above arr , we want to select row 5 , 3, 2, 4 at exact same order.
# # We pass the list [5, 3, 2, 4] into indexing.
# print(arr[[5, 3, 2, 4]])
# import numpy as np
# arr = np.arange(32).reshape(8, 4)
# print(arr)
# # Now
# print(arr[[1, 3, 5, 2], [0, 3, 1, 2]])
# This particular line will act as an coordinated indexing , i.e it will give
# us the elements which are located on (1, 0), (3, 3), (5, 1), and (2, 2).
# output will be -> array[4, 15, 21, 10]

"""
Transposing Arrays and Swapping Axes

We will do Matrix multiplication:
NOTE: keep in mind that while multiplication between two Matrix A and B, the columns of 
A matrix should be equal to the rows of B matrix, and the resultant matrix after their multiplication
will be the shape of (row of the A matrix, Column of the B matrix).
"""
# arr1 = np.arange(15).reshape(3, 5)
# print(arr1)
# # print(f"\n{arr.T}")
# arr = np.array([[0, 1, 0], [1, 2, -2], [6, 3, 2], [-1, 0, -1], [1, 0, 1]])
# print(arr)

# # We can compute the inner matrix product using (np.dot)
# print(np.dot(arr1, arr))
# # And we can also compute it by using the @ infinix Operator.
# multiplied = arr1 @ arr
# print(multiplied)

# Well we have understood that .T method will Transpose the matrix, but it's good for 
# When we handle data which is not 2D , like 3D or else , we use swapaxes(axis1, axis2) method.

# arr = np.arange(15).reshape(5, 3)
# print(arr)
# print(arr.swapaxes(0, 1)) # it means everything on the axis0 swap them into axis 1, and everything of axis1 swap them into axis0

"""
Pseudorandom Number Generation
"""
# Create a generator (the "Dealer")
# rng = np.random.default_rng(seed=43)

# # Generate 5 random floats between 0 and 1
# print(rng.random(5))

# leads = np.array(['Lead_A', 'Lead_B', 'Lead_C', 'Lead_D', 'Lead_E'])

# # Pick 3 unique leads at random (without replacement)
# sample = rng.choice(leads, size=3, replace=False)
# print(sample)

# # Permutaion Returns a new shuffled copy.
# shuffled_lead = rng.permutation(leads)
# print(leads)
# print(shuffled_lead) # This doesn't messup the original dataset.

# # Shuffle: Shuffles the data in original leads, effect the original dataset.
# rng.shuffle(leads)
# print(leads) # now the original dataset has been effected.

# # Integers: Great for Auditing. If you have 500 invoices and need to pick 5 at random to check for errors, you'd use this.
# audit_list = rng.integers(1, 100, size=(5, 2)) # we can change the size which is basically the dimension.
# print(audit_list)

# # Uniform: Great for Pricing. If you think the price of a raw material will be anywhere between ₹10 and ₹15, but you aren't sure where.
# exg_rt = rng.uniform(20.0, 25.0, size=5)
# print(exg_rt)

# # DISTRIBUTION
# # normal(mean, std_dev, size)
# # Simulate 1,000 students' exam scores (Mean=60, StdDev=10)
# scores = rng.normal(60, 10, size=1000)
# print(scores)

# # Binomial(n, p)
# # n: Number of attempts (e.g., 100 phone calls).
# # p: Probability of success (e.g., 0.05 chance they buy)
# # Simulate 10 days of calling (100 calls per day, 5% success)
# daily_sales = rng.binomial(100, 0.05, size=10)
# print(daily_sales)

"""
Universal Functions: Fast Element-Wise Array Functions.
"""
# # Many ufuncs are simple element-wise transformations, like numpy.sqrt or numpy.exp:
# arr = np.arange(10)
# print(arr)
# # np.sqrt fun
# print(np.sqrt(arr))
# # np.exp fun
# print(np.exp(arr)) # This ufuncs are called Unary Universal Function(unary ufuncs) since the take single array as input.

# # Others Functions like np.add or np.maximum, takes two arrays(thus, binary unfuncs) and return a single array as the result:
# rng = np.random.default_rng(seed=12345)

# x = rng.standard_normal(8)
# y = rng.standard_normal(8)
# # print(x)
# # print(y)

# # add = np.add(x, y)
# # print(add)

# # find_max = np.maximum(x, y)
# # print(find_max)

# arr = rng.standard_normal(7) * 5
# print(arr)

# remainder, whole_part = np.modf(arr)
# print(whole_part)
# print(remainder)

"""
Array Oriented Programming:
"""
# import math
# points = np.round(np.arange(-5, 5, 0.01), decimals=2) # 1000 equally spaced points

# # print(points)
# xs, ys = np.meshgrid(points, points)
# # print(ys)

# # print(math.sqrt(xs[(0,0)]**2 + ys[(0, 0)]**2))

# z = np.sqrt(xs ** 2 + ys ** 2)
# # print(z)

# import matplotlib.pyplot as plt

# plt.imshow(z, cmap=plt.cm.gray, extent=[-5, 5, -5, 5])
# plt.colorbar()
# plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of vlaues")
# plt.show()
# plt.close("all")

"""
Expressing Conditional Logic as Array Operations
The numpy.where function is a vectorized version of the ternary expression x if
condition else y. Suppose we had a Boolean array and two arrays of values:
"""
# xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
# yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])

# condition = np.array([True, False, True, True, False])

# # Suppose we wanted to take a value from xarr whenever the corresponding value in "condition"
# # is True, and otherwise take the value from yarr, A list comprehension doing this might look like.
# result = [x if c else y for x, y, c in zip(xarr, yarr, condition)]
# print(result)

# # With numpy.where we can do this with a single function call:

# result2 = np.where(condition, xarr, yarr)
# print(result2)

# # Suppose you had a matrix of randomly generated data and you wanted to replace all positive values
# # with 2 and all negative values with -2. This is possible to do with numpy.where
# rng = np.random.default_rng(seed=44)
# arr = rng.standard_normal((4, 4))
# print(arr)

# new_arr = np.where(arr > 0, 2, arr)
# print(new_arr)

"""
Methods for Boolean Arrays:
"""
# rng = np.random.default_rng(seed=44)
# arr = rng.standard_normal(100)

# print(arr)
# print((arr > 0).sum())
# print((arr <=0).sum())

# bool = np.where(arr>0, True, False)
# print(bool.any()) # any() method returns is wether one or more values in an array is True.
# print(bool.all()) # all() method retruns is every value is True.

"""
Sorting:
Like Python's built-in list type, NumPy arrays can be sorted in place with the sort method:
"""
# rng = np.random.default_rng(seed=44)
# arr = rng.standard_normal((5, 3))
# print(arr)

# arr.sort()
# print(arr)

"""
Linear algebra of NumPy:
"""

# x = np.array([[1, 2, 3], [4, 5, 6]])
# y = np.array([[6, 23], [-1, 7], [8, 9]])

# print(x.dot(y)) # x.dot(y) is equivalent to np.dot(x, y)

# h = np.ones(3)
# print(x @ h)

"""
Example: Random Walk
The simulation of random walks provides an illustrative application of utilizing array
operations. Let's first consider a simple random walk starting at 0 with steps of 1 and-1 
occurring with equal probability.
"""

# Here is a pure Python way to implement a  single random walk with 1,000 steps using the 
# built-in random module:

# #! blockstart
# import random
# position = 0
# walk = [position]
# nsteps = 1000
# for _ in range(nsteps):
#     step = 1 if random.randint(0, 1) else -1
#     position += step
#     walk.append(position)
# #! blockend
# # print(walk)

# import matplotlib.pyplot as plt

# plt.plot(walk[: 100])
# plt.show()

n_walks = 5000
n_steps = 1000
draws = np.random.randint(0, 2, size=(n_walks, n_steps))
# print(draws)

steps = np.where(draws > 0, 1, -1)
# print(steps)

walk = np.cumsum(steps, axis=1)
# print(walk)

# import matplotlib.pyplot as plt

# plt.plot(walk)
# plt.show()
print(walk.min())