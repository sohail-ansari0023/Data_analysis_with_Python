## Data Cleaning and Preparation

### Handling Missing values

Before a machine leanrning model can find patterns in data, the data must be mathematically sound. Most ML algorithms(like those in Scikit-Learn) will throw a fatal error if the data has missing values.

In Pandas, missing values usually shows as `NaN` (Not a Number) or `None`.

#### Filtering Out Missing Data(or dropping)

well it is the simplest ways to handle this, but it must be done strategically. if we just delete everything that has a blank cell, we might throw away 80% of valuable dataset.
 
**HOW WE WILL DO IT:**
- **Step 1:** The Diagnosis(Finding the Missing Data)
    - A good analyst never deletes data blindly. First, we must quantify the damage. 
- **Step 2:** The Nuclear Option(Dropping any row with a missing value)
    - The most basic method is to drop a row entirely if it is missing  even one piece of information. we use the `dropna()` method for this.