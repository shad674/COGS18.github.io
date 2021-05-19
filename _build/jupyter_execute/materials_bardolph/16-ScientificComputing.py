**Course Announcements**

- **CL7** due tonight

**Notes**
- E2 scores posted; answer key available on website
- Additional OH and coding lab link added to main canvas page
- A5 now available (we have not yet covered all material; due 5/31)

**Q&A**

Q: Wait...what's the difference between scripts and modules again?  
A: Scripts are for *executing/running* code. When you execute a script, the code inside that .py file gets run from top to bottom. Scripts are for accomplishing a task with code. Modules are for *storing* code. The code inside a module can be *imported* elsewhere to be used. Modules are for storing code so that it's available to you when you want it.

Q: And, why do we create modules anyway instead of just having the code in our notebooks?  
A: This allows you to reuse the code anywhere you want. In a notebook, the code is a bit "stuck" so it can only be used in one location - that notebook.

Q: Help! The terminal confuses me  
A: Definitely go to coding lab today! That's a focus this week!

Q: How do you submit a folder on datahub for the final project?  
A: When you click "submit" on datahub, all of the files in the folder where the assignment is stored will be submitted. It will *look* like only the notebook is being submitted, but I promise all files in that folder will be submitted.

Q: When we download a game onto our computers, are we essentially downloading a bunch of modules or a package?  
A: Sometimes! There are different ways in which games are designed, but this is one approach! 

Q: When would we see the `from module import *`? I was curious when this would show up since we didn't do an example like that in class.  
A: When people are being lazy :) 

Q: why do we need to know command lines and what are we going to use them for?  
A: You'll want to know the basic shell commands discussed in lecture. You'll use this to navigate files on datahub. Note that you probably *could* get through this course without learning them; however, learning them will save you tons of time in your every day life if you get comfortable with them!

Q: How does one know what modules are already installed in the notebook before attempting to import them?  
A: https://docs.python.org/3/library/  

Q: If we use modules from python standard library, do we need to write quotation(such as using MLA format) for it?  A: https://cogs18.github.io/projects/faq.html#citations 

Q: What happens if you import two different choice functions? Which one would run if you used the choice function? 
A: The one you most recently imported.

Q: Will we need to have a method for the final project?  
A: Nope you will need some total of 3 functions or methods. (If you meant to ask about modules, you'll need either a module or a script.)

# Scientific Computing

<div class="alert alert-success">
<b>Scientific Computing</b> is the application of computer programming to scientific applications: data analysis, simulation & modelling, plotting, etc. 
</div>

## Scientific Python: Scipy Stack

Scipy = Scientific Python

- `scipy`
- `numpy`
- `pandas`
- Data Analysis in Python

<div class="alert alert-success">
<b><code>Scipy</code></b> is an <i>ecosystem</i>, including a collection of open-source packages for scientific computing in Python.
</div>

A 'family' of packages that all work well together to do scientific computing.

Not made by the same people who manage the standard library.

## Homogenous Data

- for example: store data of the same type (i.e. all numerics)
- recordings of values from experimental participants
- heights or quantitative information from survey data

Lists are a start, and lists of lists are possible.

But, they can get nightmareish.

So we use arrays.

### `numpy`

**`numpy`** - stands for numerical python

**arrays** - work with arrays (matrices)

Allow you to efficiently operate on arrays (linear algebra, matrix operations, etc.)

import numpy as np

# Create some arrays of data
arr0 = np.array([1, 2, 3])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

arr1

# lists of lists don't store dimensionality well
[[1, 2], [3, 4]] 

#### Indexing Arrays

# Check out an array of data
arr1

`numpy` arrays are an object type...so they have associated attributes (below) and methods (we'll get to these in a second)!

# Check the shape of the array
arr1.shape

# Index into a numpy array
arr1[0, 0]

Working with N-dimensional (multidimensional) arrays is easy within `numpy`.

#### Notes on Arrays

# arrays are most helpful when they
# have the same length in each list
np.array([[1, 2, 3, 4], [2, 3, 4]])

# arrays are meant to store homogeneous data
np.array([[1, 2, 'cogs18'], [2, 3, 4]])

#### Working with Arrays

(Things you can't do with lists)

# Add arrays together
arr1 + arr2

# Matrix mutliplication
arr1 * arr2

#### A brief aside: `zip()`

`zip()` takes two iterables (things you can loop over) and loop over them together.

for a, b in zip([1,2], ['a','b']):
    print(a, b)

#### Clicker Question #1

Given the following code, what will it print out?

data = np.array([[1, 2, 3, 4],
                 [5, 6, 7, 8]])
 
output = []
for d1, d2 in zip(data[0, :], data[1, :]):
    output.append(d1 + d2)

print(output)

- A) [1, 2, 3, 4]
- B) [1, 2, 3, 4, 5, 6, 7, 8]
- C) [6, 8, 10, 12]
- D) [10, 26]
- E) [36]

Note that if you find yourself looping over arrays...there is probably a better way.

# sum method
# by default sums all values in array
data.sum()

# sum method
# has an axis parameter
# axis=0 sums across columns
data.sum(axis=0)

# typecasting to a different variable type
out_list = data.sum(axis=0).tolist()
print(out_list)
type(out_list)

What if you wanted to find the max value in an array...there's a method for that!

# find max value in array
max_val = data.max()
max_val

But what if you wanted to know not what the max value was...but where in your original array that value was found. 

There are also *functions* in `numpy` that operate on arrays. 

# see documentation for np.where()
np.where?

# find position in array with max value
out = np.where(data == max_val)
out

# check to be sure
data[1,3]

## Heterogenous Data

- have continuous (numeric) and categorical (discrete) data
- different data types need to be stored
- uses a DataFrame object (think: spreadsheet)
- allows for column and row labels

### pandas

Pandas is Python library for managing heterogenous data.

At it's core, Pandas is used for the **DataFrame** object, which is:
- a data structure for labeled rows and columns of data
- associated methods and utilities for working with data.
- each column contains a `pandas` **Series**

import pandas as pd

# Create some example heterogenous data
d1 = {'Subj_ID': '001', 'score': 16, 'group' : 2, 'condition': 'cognition'}
d2 = {'Subj_ID': '002', 'score': 22, 'group' : 1, 'condition': 'perception'}
d3 = {'Subj_ID': '003', 'score': 18, 'group' : 1, 'condition': 'perception'}

# Create a dataframe 
df = pd.DataFrame([d1, d2, d3], [0, 1, 2])

# Check out the dataframe
df

# You can index in pandas
# columns store information in series
df['condition']

# You can index in pandas
# loc specifies row, column position
df.loc[0,:]

# attribute of df object
# row, columns
df.shape

#### Working with DataFrames

There are *a lot* of functions and methods within `pandas`. The general syntax is `df.method()` where the `method()` operates directly on the dataframe `df`.

# calculate summary statistics
df.describe()

# Take the average of all numeric columns
df.mean()

# breakdown of how many of each category there are
val_counts = df['condition'].value_counts()
val_counts

# which unique values are there in condition? 
df['condition'].unique()

# how many unique values are there
len(df['condition'].unique())
# equivalent to
df['condition'].nunique()

# how many rows there are in a series/df
len(df)

# what's the category that shows up the most 
val_counts.idxmax()

# what's the count of the value that shows up the most
val_counts.max()

#### Clicker Question #2

Comparing them to standard library Python types, which is the best mapping for these new data types?

- A) DataFrames are like lists, arrays are like tuples
- B) DataFrames and arrays are like lists
- C) DataFrames are like tuples, arrays are like lists
- D) DataFrames and arrays are like dictionaries
- E) Dataframes are like dictionaries, arrays are like lists

## Plotting

%matplotlib inline

import matplotlib.pyplot as plt

# Create some data
dat = np.array([1, 2, 4, 8, 16, 32])

# Plot the data
plt.plot(dat);

- can change plot type
- _lots_ of customizations possible

## Analysis

- `scipy` - statistical analysis
- `sklearn` - machine learning

import scipy as sp
from scipy import stats

# Simulate some data
d1 = stats.norm.rvs(loc=0, size=1000)
d2 = stats.norm.rvs(loc=0.5, size=1000)

### Analysis - Plotting the Data

# Plot the data
plt.hist(d1, 25, alpha=0.6);
plt.hist(d2, 25, alpha=0.6);

### Analysis - Statistical Comparisons

# Statistically compare the two distributions
stats.ttest_ind(d1, d2)

## COGS108: Data Science in Practice

<div class="alert alert-info">
If you are interested in data science and scientific computing in Python, consider taking <b>COGS108</b> : <a>https://github.com/COGS108/</a>.
</div>