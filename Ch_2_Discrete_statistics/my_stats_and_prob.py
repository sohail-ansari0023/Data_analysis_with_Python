"""
In this Script there will be programs for some stats and prob
functions, such as: odds in favour, prob, prob with respect to
odds in favor. standard deviations and etcetra.
"""

# odds in favor
def odds(favorable, unfavorable):
    """
    favorable = total number of favorable outcomes.
    unfavorable = total number of unfavorable outcomes.
    and we know:
       odds in favor = favorable upon unfavorable.
    """
    return favorable / unfavorable

# probability of an event.
def probability(favorable, unfavorable):
    """
    as we know:
        probability = favorable / total outcomes.
        total outcomes = favorable + unfavorable
    """
    return favorable / (favorable + unfavorable)

#-------------------------------------------
# FREQUENCY HISTOGRAM FUNCTION
#-------------------------------------------
"""
The most common representation of a distribution is a histogram, which is
a graph that shows the frequency or probability of each value.
"""

# data_list = [5, 3, 5, 5, 3 ,4 ,4 ,4, 6, 5, 3] # My data.
"""
In Python, an efficient way to compute frequencies is with a dictionary
"""
# hist = {}
# for x in data_list:
#      hist[x] = hist.get(x, 0) + 1

#------------------------------------
# NORMALIZATION
#------------------------------------
"""
The result is a dictionary that maps from values to frequencies. To get from
frequencies to probabilities, we divide through by n (n= total number of items),
which is called normalization.
"""
# n = float(len(data_list))
# pmf = {}
# for x, freq in hist.items():
#     pmf[x] = round(freq / n, 2)
# print(pmf)

dict = {"myname": "sohail", "hello": "Timer"}

for x in dict.values():
    print(x)

print([x for x in dict.values()])