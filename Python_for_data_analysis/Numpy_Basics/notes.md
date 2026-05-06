# Numpy Basics: Arrays and Vectorized Computation

One of the reasons NumPy is so important for numerical computations in Python is
because it is designed for efficiency on large arrays of data. There are a number of
reasons for this:

- NumPy internally stores data in a contiguous block of memory, independent of other built-in Python objects. NumPy’s library of algorithms written in the C language can operate on this memory without any type checking or other overhead. NumPy arrays also use much less memory than built-in Python sequences.

- NumPy operations perform complex computations on entire arrays without the
need for Python for loops, which can be slow for large sequences. NumPy is
faster than regular Python code because its C-based algorithms avoid overhead present with regular interpreted Python code.

## 4.1 The NumPy ndarray: A Multidimensional Array object

One of the key features of NumPy is its N-dimensional array object, or ndarray, which is a fast, flexible container for large datasets in Python. Arrays enable you to perform mathematical operations on whole blocks of data using similar syntax to the equivalent operations between scalar elements

## Creating ndarrays
The easiest way to create an array is to use the array function. This accepts any sequence-like object (including other arrays) and produces a new NumPy array containing the passed data

## Arithmetic With NumPy Arrays.
Arrays are important because they enable you to express batch operations on data without writing any **for**   loops. NumPy users call this vectorization. Any arithmetic operations between equal-size arrays apply the operation element-wise:

#### we have covered.
ARRAYS of the same size.
- Addition between arrays.
- Multiplications between arrays.
- Inversing.
- Division.
- Squaring, Exponential.

**NOTE:-** Evaluating Operations between differently sized arrays is called _Broadcasting_.

## Basic Indexing And Slicing.
NumPy array indexing is a deep topic, as there are many ways you may want to select a subset of your data or individual elements. One-dimensional arrays are simple; on the surface they act similarly to Python lists:

## Fancy Indexing
Fancy indexing is a term adopted by NumPy to describe indexing using integer arrays.

## Transposing Arrays and Swapping Axes.
Transposing is a special form of reshaping that similarly reurns a view on the underlying data without copying anything. Arrays have the **transpose** method and the special **T** attribute.

## Pseudorandom Number Generation
Randomness in computing is a bit of a magic trick. Computers are naturally logical and predictable, so to get "random" numbers, they use mathematical formulas to create a sequence that looks random but is actually determined by a starting point. This is why we call it Pseudorandom.

## Universal Functions: Fast Element-Wise Array Functions
A universal function, or ufunc, is a function that performs element-wise operations on data in ndarrays. You can think of them as fast vectorized wrappers for simple functions that take one or more scalar values and produce one or more scalar results.

<details>
<summary>Click to expand: Unary NumPy Operations Table</summary>

| Function | Description | Business/Data Use Case |
| :--- | :--- | :--- |
| **`abs`, `fabs`** | Absolute value element-wise. | Finding "Profit/Loss" magnitude. |
| **`sqrt`** | Square root (equivalent to `arr ** 0.5`). | Calculating Risk/Standard Deviation. |
| **`square`** | Square (equivalent to `arr ** 2`). | Calculating Variance for stock models. |
| **`exp`** | Compute $e^x$. | Compound Interest & growth modeling. |
| **`log`, `log10`, `log2`** | Natural, base 10, and base 2 logs. | Fixing skewed data (like income/wealth). |
| **`sign`** | Sign: 1 (+), 0 (0), or -1 (-). | Creating a "Market Direction" indicator. |
| **`ceil`** | Smallest integer $\geq$ value. | Inventory planning (rounding up units). |
| **`floor`** | Largest integer $\leq$ value. | Calculating completed sales cycles. |
| **`rint`** | Round to nearest integer. | Cleaning survey/rating data. |
| **`modf`** | Split fractional and integral parts. | Separating Rupees and Paise. |
| **`isnan`** | Check for **NaN** (Not a Number). | Finding gaps in **Sol Energy Ltd** data. |
| **`isfinite`, `isinf`** | Check for finite/infinite values. | Preventing "Divide by Zero" crashes. |
| **`cos`, `sin`, `tan`** | Trigonometric functions. | Analyzing seasonal business cycles. |
| **`arccos`, `arcsin`** | Inverse trigonometric functions. | Geometric data extraction/OCR. |
| **`logical_not`** | Compute `not x` (inverse). | Filtering out unwanted data entries. |

</details>

<details>
<summary><b>Click to expand: Binary NumPy Operations Table</b></summary>

| Function | Description | Business/Data Use Case |
| :--- | :--- | :--- |
| **`add`** | Add corresponding elements in arrays. | Consolidating revenue from multiple branches or product lines. |
| **`subtract`** | Subtract elements in second array from first array. | Calculating **Net Profit** (Revenue - Expenses). |
| **`multiply`** | Multiply array elements. | Calculating total costs: `Quantity * Unit Price`. |
| **`divide`, `floor_divide`** | Divide or floor divide (truncating remainder). | Calculating **Earnings Per Share (EPS)** or batch units. |
| **`power`** | Raise elements in first array to powers in second. | Computing **Compound Interest** or TVM. |
| **`maximum`, `fmax`** | Element-wise maximum; `fmax` ignores **NaN**. | Finding the **"Day High"** for a stock or top employee. |
| **`minimum`, `fmin`** | Element-wise minimum; `fmin` ignores **NaN**. | Finding the **"Day Low"** or lowest material costs. |
| **`mod`** | Element-wise modulus (remainder of division). | Identifying "Odd-Lot" trades or scheduling cycles. |
| **`copysign`** | Copy sign of 2nd argument to values in 1st. | Applying market "Sentiment" to a price change. |
| **`greater`, `greater_equal`**, etc. | Perform element-wise comparison ($>$, $\geq$, $<$, $\leq$, $==$, $!=$). | Setting automated **Buy/Sell triggers** or budget alerts. |
| **`logical_and`** | Element-wise truth value of **AND** (`&`). | Filtering leads: (Calls > 10) AND (Interested == True). |
| **`logical_or`** | Element-wise truth value of **OR** (`|`). | Identifying "High Priority" leads: (Large) OR (Urgent). |
| **`logical_xor`** | Element-wise truth value of **XOR** (`^`). | Finding anomalies where only one of two flags is present. |

</details>

## Array-Oriented Programming with Arrays
