# Getting Started with Pandas
## Introduction to pandas Data Structures
To get started with pandas, you will need to get comfortable with its two workhorse data structures: Series and DataFrame. While they are not a universal solution for every problem, they provide a solid foundation for a wide variety of data tasks.

### Series
A Series is one-dimensional array-like object containing a sequence of values (of similar types) and an associated array of data labels, called its index.

### DataFrame
A DataFrame represents a rectangular table of data and contains an ordered, named collection of columns, each of which can be a different value type (numeric, string, Boolean, etc.). The DataFrame has both a row and column index; it can be thought of as a dictionary of Series all sharing the same index.

### Index Objects
pandas’s Index objects are responsible for holding the axis labels (including a Data Frame’s column names) and other metadata (like the axis name or names). Any array or other sequence of labels you use when constructing a Series or DataFrame is internally converted to an Index:

### Essential Functionality
This section will walk you through the fundamental mechanics of interacting with the data contained in a Series or DataFrame. In the chapters to come, we will delve more deeply into data analysis and manipulation topics using pandas. This book is not intended to serve as exhaustive documentation for the pandas library; instead, we’ll focus on familiarizing you with heavily used features, leaving the less common (i.e., more esoteric) things for you to learn more about by reading the online pandas
documentation.

### Droping Entries from an Axis
Dropping one or more entries from an axis is simple if you already have an index array or list without those entries, since you can use the reindex method or .loc based indexing. As that can require a bit of munging and set logic, the drop method will return a new object with the indicated value or values deleted from an axis:

### Indexing, Selection, and Filtering
Series indexing (obj[....]) works analogously to NumPy array indexing, except you can use the Series's index values instead of only integers. Here are some examples of this:
