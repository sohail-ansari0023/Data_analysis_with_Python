"""
IN THIS WE WILL SEE SOME PRACTICE QUESTIONS USING THE REAL WORLD DATA.
"""
import numpy as np

"""EXERCISE ONE:"""
#-------------------------------------------------------------------------------
# You are analyzing lap times from recent Grand Prix session. You have an array
# representing your lap times (in seconds) for three different drivers accross
# five laps. each row is a driver and each column is a lap time.
#------------------------------------------------------------------------------

# Rows = Driver A, Driver B, Driver C
# Columns = Laps (lap 1 to lap 5)
# lap_times = np.array([
#     [82.5, 81.2, 80.8, 81.0, 80.5],
#     [83.1, 82.0, 81.5, 81.8, 81.1],
#     [81.9, 81.1, 80.2, 80.7, 80.1]
# ])

# # TASK 1: Broadcasting: The track temperature dropped, 
# # and the sensor was miscalibrated by 0.3 seconds for everyone.
# # Deduct 0.3 seconds from every single lap time in one line of code.

# new_lap_times = lap_times - 0.3
# # print(new_lap_times)

# # TASK 2: Aggregation: Find the fastest (minimum) lap time for each driver. 
# # (Hint: look at the axis parameter).

# # Fastest lap time for
# driv_A = new_lap_times[0].min()
# driv_B = new_lap_times[1].min()
# driv_C = new_lap_times[2].min()

# # print(f"The fastest lap time for:\nDriver A:{driv_A} sec\nDriver B: {driv_B} sec\nDriver C: {driv_C} sec")

# # TASK 3: Boolean Masking: The team boss only wants to look at "qualifying pace."
# #  Create a new array that extracts only the lap times that are strictly under 81.0 seconds.

# new_arr = np.where(new_lap_times <= 81.0, True, False)
# # print(new_arr)

"""EXERCISE TWO:"""
#---------------------------------------------------------------------------------------
# You are building an automation tool to track daily stock prices. You have a 1D array
# representing the closing price of a single stock over 10 consecutive trading days.
#---------------------------------------------------------------------------------------

# prices = np.array([150.0, 152.5, 149.0, 155.0, 157.2, 156.0, 159.5, 162.0, 160.1, 165.0])

# # TASK 1: Calculate the absolute daily price change (the difference between day n 
# # and day n-1). You should end up with an array of 9 values. (Hint: look up np.diff)

# daily_changes = np.diff(prices)
# # print(daily_changes)

# # TASK 2: Convert those absolute daily changes into percentage changes relative to the previous day's price.

# per_changes = (daily_changes / prices[:-1]) * 100
# # print(np.round(per_changes, 2))

# # TASK 3: The "Where" Logic: Create a new array of strings where every positive return day 
# # is marked as "Gain" and every negative return day is marked as "Loss".

# new_array = np.where(per_changes > 0, "Gain", "Loss")
# print(new_array)

"""EXERCISE THREE:"""
#--------------------------------------------------------------------------------------------------
# Let's take the Random Walk concept to the next level. Instead of simulating one path, 
# you are going to simulate the price action of 5 different assets simultaneously over 100 days
#--------------------------------------------------------------------------------------------------

# np.random.default_rng(seed=42)

# # generate a (5 x 100) matrix of random steps: either 1 or -1.
# raw_steps = np.where(np.random.randint(0, 2, size=(5, 100)) > 0, 1, -1)
# # print(raw_steps)

# # Starting price of all 5 assets is $100.
# start_price = np.full((5, 1), 100)
# # print(start_price)

# # TASK 1: Transform the raw_steps matrix into a matrix of continuous price paths using np.cumsum.

# cont_price = np.cumsum(raw_steps, axis=1)
# # print(cont_price)

# # TASK 2: Add the starting_prices to your paths so that every asset starts at $100 and moves from there.
# price_path = start_price + cont_price
# print(price_path)

# # TASK 3: Slice the final matrix to extract only the final day's price (the very last column) for all 5
# # assets to see where they ended up.
# final_day_price = price_path[ : , -1:]
# print(final_day_price)