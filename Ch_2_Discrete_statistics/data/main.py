import os 
# import urllib.request

# These are the official 2002 (Cycle 6) URLs
# import urllib.request

# # These are the ACTIVE links from the official ThinkStats2 repo
# files = {
#     "nsfg2.py": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/nsfg.py",
#     "thinkstats2.py": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/thinkstats2.py",
#     "2002FemPreg.dct": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/2002FemPreg.dct",
#     "2002FemResp.dct": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/2002FemResp.dct"
# }

# for filename, url in files.items():
#     try:
#         urllib.request.urlretrieve(url, filename)
#         print(f"✅ {filename} downloaded.")
#     except Exception as e:
#         print(f"❌ Failed {filename}: {e}")

# files = ['nsfg2.py', 'thinkstats2.py', '2002FemResp.dat.gz', '2002FemResp.dct']

# for f in files:
#     if os.path.exists(f):
#         print(f"{f} is ready!")
#     else:
#         print(f"{f} is missing!")

# import urllib.request

# # The official raw links for the dictionary files
# dct_files = {
#     "2002FemPreg.dct": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/2002FemPreg.dct",
#     # "2002FemResp.dct": "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/2002FemResp.dct"
# }

# for filename, url in dct_files.items():
#     print(f"Downloading {filename}...")
#     try:
#         urllib.request.urlretrieve(url, filename)
#         print(f"✅ Successfully saved {filename}")
#     except Exception as e:
#         print(f"❌ Failed to download {filename}: {e}")

# print("\nAll done! Check your folder now.")
# import urllib.request

# url = "https://raw.githubusercontent.com/AllenDowney/ThinkStats2/master/code/thinkplot.py"
# filename = "thinkplot.py"

# try:
#     print(f"Downloading {filename}...")
#     urllib.request.urlretrieve(url, filename)
#     print(f"✅ Successfully saved {filename}!")
# except Exception as e:
#     print(f"❌ Error: {e}")
# import nsfg2

# preg = nsfg2.ReadFemPreg()
# resp = nsfg2.ReadFemResp()

# print("pregnancy data rows:", len(preg))
# print("respondent data rows:", len(resp))

# try:
#     import pandas as pd
#     import matplotlib.pyplot as plt
#     import nsfg2
#     import thinkstats2
#     import thinkplot
    
#     print("✅ All Libraries (Pandas, Matplotlib) are installed!")
#     print("✅ All Book Modules (nsfg2, thinkstats2, thinkplot) are found!")
    
#     # Final Test: Load the data
#     preg = nsfg2.ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz' )
#     print(f"🚀 Success! Loaded {len(preg)} pregnancy records.")

# except ModuleNotFoundError as e:
#     print(f"❌ Missing: {e}")
#     print("Hint: If it's matplotlib or pandas, use 'pip install'. If it's a .py file, download it to your folder.")
# except Exception as e:
#     print(f"❌ An error occurred: {e}")

import nsfg2

# preg_ = nsfg2.ReadFemPreg(dct_file='2002FemPreg.dct', dat_file='2002FemPreg.dat.gz' )
# # print(f"🚀 Success! Loaded {len(preg)} pregnancy records.")

# # Create a clean, de-fragmented copy
# preg = preg_.copy()
# # Now you can work with 'preg' without the warning appearing
# print("DataFrame de-fragmented!")

# # 1. Filter for only live births (outcome == 1)
# live = preg[preg.outcome == 1]
# print(f"Total live Births: {len(live)}")

# # 2. Split the data into 'First Babies' and 'Others'
# firsts = live[live.birthord == 1]
# others = live[live.birthord > 1]

# print(f"First Babies: {len(firsts)}")
# print(f"Other Babies: {len(others)}")

# # 3. Compare the average pregnancy lenght (in weeks)
# print(f"\nAvg. pregnancy length (Firsts): {firsts.prglngth.mean():.2f} weeks")
# print(f"\nAvg. pregnancy length (Others): {others.prglngth.mean():.2f} weeks")

# import time
preg_ = nsfg2.ReadFemPreg()
# resp_ = nsfg2.ReadFemResp()

# De-Fregmented.
preg = preg_.copy()
# resp = resp_.copy()

print(f"Success! Loaded {len(preg)} Pregnancy records.")
# print(f"Success! Loaded {len(resp)} Responded records.")
# print(f"Number of columns in Pregnancy records: {len(preg.columns)}")
# print(f"Number of columns in Responded records: {len(resp.columns)}")

# start_time_1 = time.time()
# count = 0
# for live_births in preg['outcome']:
#     if live_births is 1:
#         count += 1
# end_time_1 = time.time()

# execution_time_1 = end_time_1 - start_time_1

# start_time_2 = time.time()
# # Using the pandas value_counts() methods, 
# end_time_2 = time.time()

# execution_time_2 = end_time_2 - start_time_2

# print(f"total live birth found by loop {count} live births.")
# print(f"total live birth found by value_counts() method: {preg.outcome.value_counts()[1]}")

# print(f"loop takes {execution_time_1} sec, whereas the pandas value_counts() method takes {execution_time_2} sec, Difference {execution_time_1 - execution_time_2}")


# def live_birth_order(data):
#     live_count = 0   # this will show total count
#     first_babies_live_count = 0   # this will show to live counts who are the first one.
#     other_babies_live_count = 0   # this will show to live counts who are the other one.
#     for index in range(len(data['outcome'])):
#         if data['outcome'][index] == 1:
#             live_count +=1
#             if data['birthord'][index] == 1.0:
#                 first_babies_live_count += 1
#             else:
#                 other_babies_live_count += 1
#         else:
#             continue
    
#     if live_count == first_babies_live_count + other_babies_live_count:
#         print("Successs!")
#     else:
#         print("There's sum miss match.")

#     print(f"Total live counts: {live_count}")
#     print(f"Total First baby live count: {first_babies_live_count}")
#     print(f"Total other babies live count: {other_babies_live_count}")

# live_birth_order(preg)

# other way.
# def live_birth_count_2(data):
#     live = data[data.outcome == 1]
#     first_count = (live.birthord == 1).sum()
#     others_count = (live.birthord > 1).sum()
    
#     return [first_count, others_count]

# result = live_birth_count_2(preg)
# print(f"First Babies: {result[0]}, Other babies: {result[1]}")

first_babies = preg[preg.birthord == 1]
other_babies = preg[preg.birthord > 1]
avg_pl_first_babies = first_babies.prglngth.mean()
avg_pl_other_babies = other_babies.prglngth.mean()

print(f"The average pregnancy length (in weeks) for first babies is: {avg_pl_first_babies}")
print(f"The average pregnancy length (in weeks) for other babies is: {avg_pl_other_babies}")