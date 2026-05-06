import empiricaldist
import numpy as np 
import matplotlib.pyplot as plt
# from thinkstats2 import decorate
import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=pd.errors.PerformanceWarning)


from nsfg2 import ReadFemPreg

preg = ReadFemPreg()

live_birth = preg[preg.outcome == 1]
print(live_birth['outcome'].count())

ftab_lb = FreqTab.from_seq(live_birth['birthwht_lb'], name="birthwgt_lb")