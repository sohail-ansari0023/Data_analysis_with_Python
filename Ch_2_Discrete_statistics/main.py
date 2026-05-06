# import urllib.request

# url = "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/thinkstats2.py"
# filename = "thinkstats2.py"

# try:
#     print(f"Downloading {filename}...")
#     urllib.request.urlretrieve(url, filename)
#     print(f"✅ Successfully saved {filename}!")
# except Exception as e:
#     print(f"❌ Error downloading: {e}")

# import urllib.request

# url = "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/thinkplot.py"
# filename = "thinkplot.py"

# try:
#     print(f"Downloading {filename}...")
#     urllib.request.urlretrieve(url, filename)
#     print(f"✅ Success! thinkplot.py is ready.")
# except Exception as e:
#     print(f"❌ Download failed: {e}")

# import thinkstats2
# import math

# def pumpkin():
#     # 1. Create the list of weights.
#     # 3 decorative (1lb), 2 pie (3lb), 1 Atlantic Giant (591).
#     weights = [1, 1, 1, 3, 3, 591]

#     mu = thinkstats2.Mean(weights)
#     var = thinkstats2.Var(weights, mu=mu)

#     # standard deviation is the square root of variance(sigma)
#     std = math.sqrt(var)

#     print("--------Pumpkin stats------------")
#     print(f"Mean (Average) : {mu:.2f}lbs")
#     print(f"Variance (σ²) : {var:.2f}lbs")
#     print(f"Standard Deviation (σ) : {std:.2f}lbs")

# pumpkin()
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)

# ... the rest of your code
import nsfg2
import thinkstats2
import math

# preg_ = nsfg2.ReadFemPreg()

# # Defregmenting
# preg = preg_.copy()

# print(f"Success! Loaded {len(preg)} Pregnancy records.")

# # The value {1.0} defines the first child birth.
# first_babies = preg[preg.birthord == 1.0]
# other_babies = preg[preg.birthord > 1.0]


# def std_first_babies(data):
#     # Average gestation time for first babies.
#     mean_first = thinkstats2.Mean(data['prglngth'])
#     # Variance of first babies.
#     var = thinkstats2.Var(data['prglngth'], mu=mean_first)
#     # standard deviation of gestation time for first babies.
#     # (just the square root of variance)
#     std_first_babies = math.sqrt(var)

#     return [mean_first, var, std_first_babies] 

# def std_other_babies(data):
#     # Average gestation time for other babies.
#     mean_others = thinkstats2.Mean(data['prglngth'])
#     # Variance of other babies.
#     var = thinkstats2.Var(data['prglngth'], mu=mean_others)
#     # standard deviation of gestation time for other babies.
#     # (just the square root of variance)
#     std_other_babies = math.sqrt(var)

#     return [mean_others, var, std_other_babies] 

# result_1 = std_first_babies(data=first_babies)
# result_2 = std_first_babies(data=other_babies)

# print(f"----------------Final Result----------------")
# print(f"\nFirst Babies:---")
# print(f"Mean of gestation periof for first babies: {result_1[0]:.2f} Weeks")
# print(f"Variance of gestation period for first babies: {result_1[1]:.2f} Weeks")
# print(f"Standard deviation of gestation period for first babies: {result_1[2]:.2f} Weeks")
# print(f"\nOther Babies:---")
# print(f"Mean of gestation periof for first babies: {result_2[0]:.2f} Weeks")
# print(f"Variance of gestation period for first babies: {result_2[1]:.2f} Weeks")
# print(f"Standard deviation of gestation period for other babies: {result_2[2]:.2f} Weeks")
# import operator

# def AllMode(hist):
#     """Returns a list of value-frequency pairs in descending order of frequency.
#     hist: Hist object (which acts like a dictionary)
#     """
#     # 1. Get the itmes from the Hist (value, frequency)
#     items = hist.Items()

#     # 2. Sort the items.
#     # key=operator.itemgetter(1) means "sort by the second element" (the frequency).
#     # reverse=True means "descending order" (highest frequency first).
#     sorted_items = sorted(items, key=operator.itemgetter(1), reverse=True)
    
#     return sorted_items

# data_list = [4, 5, 6, 2, 6, 3, 5, 3, 3, 5, 6, 6, 6, 8, 4,4 ,8]
# hist = thinkstats2.Hist(data_list)

# modes = AllMode(hist=hist)

# # print("--- All modes (value, Frequency)---")
# # for val, freq in modes:
# #     print(f"value: {val} | Count: {freq}")

# import matplotlib.pyplot as pyplot

# val, freqs = hist.Render()
# rectangles = pyplot.bar(val, freqs)
# pyplot.show()

