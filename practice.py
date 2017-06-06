# This file based on a tutorial from https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dsintro

import numpy as np
import pandas as pd

#############################################################################################################
# Series
#############################################################################################################

# Series is a one-dimensional labeled array capable of holding any data type (integers, strings,
# floating point numbers, Python objects, etc.). The axis labels are collectively referred to as the index.

# ***********************************************************************************************************
# Declare Series
# ***********************************************************************************************************

# The basic method to create a Series is to call:
# s = pd.Series(data, index=index)
# data can be dictionary, ndarray, scalar value

# -----------------------------------------------------------------------------------------------------------
# If data is an array
# -----------------------------------------------------------------------------------------------------------

# index must be the same length as data
# otherwise: ValueError: Wrong number of items passed 5, placement implies 4

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print('\n s: \n')
print(s)
print('\n s.index: \n')
print(s.index)

# You can create Series without index, in this case, it is autocreated: [0, ..., len(data) - 1]

s2 = pd.Series(np.random.randn(5))
print('\n s2: \n')
print(s2)

# -----------------------------------------------------------------------------------------------------------
# If data is a dictionary
# -----------------------------------------------------------------------------------------------------------

# keys will be the indexes

d = {'a': 0., 'b': 1., 'c': 2.}

# If you don't give index, the sorted list of keys will be the index
# But you can give the order of keys as index
# If you give extra key, which is not in the dictionary, it's value will be NaN
# If you skip existing key, It simple skip it, won't throw ValueError

s3 = pd.Series(d, index=['b', 'd', 'c'])
print('\n s3: \n')
print(s3)

# -----------------------------------------------------------------------------------------------------------
# If data is a scalar value
# -----------------------------------------------------------------------------------------------------------

# In this case an index must be provided. The value will be repeated to match the length of index
# If you don't give an index, the series will contain the data once with index 0

s4 = pd.Series(5., index=['a', 'b', 'c', 'd', 'e'])
print('\n s4: \n')
print(s4)

# ***********************************************************************************************************
# Access and modification of Series Elements
# ***********************************************************************************************************

# You can do it like in the case of arrays:

print('\n s[0]: \n')
print(s[0])

print('\n s[:3]: \n')
print(s[:3])

print('\n s[s > s.median()]: \n')
print(s[s > s.median()])

print('\n s[[4, 3, 1]]: \n')
print(s[[4, 3, 1]])

print('\n np.exp(s): \n')
print(np.exp(s))

s[0] = '1.1'
print(s)

# Or like in case of dictionaries:

print("\n s['a']: \n")
print(s['a'])

s['e'] = 12.
print(s)

print("\n 'e' in s: \n")
print('e' in s)

# If you try to get a non-existing element for example: s['f'], you get KeyError
# But if you use the get method, you get None

print("\n get 'f' which is not in the series: \n")
print(s.get('f'))

# ***********************************************************************************************************
# Vectorized operations and label alignment with Series
# ***********************************************************************************************************

# When doing data analysis, as with raw NumPy arrays looping through Series value-by-value is usually not necessary.
# Series can also be passed into most NumPy methods expecting an ndarray.

print("\n s+s: \n")
print(s+s)

print("\n s*2: \n")
print(s*2)

# Operations between Series automatically align the data based on label
# If a label is not found in one Series or the other, the result will be marked as missing NaN

print("\n s[1:] + s[:-1]: \n")
print(s[1:] + s[:-1])

#############################################################################################################
# DataFrame
#############################################################################################################

# DataFrame is a 2-dimensional labeled data structure with columns of potentially different types.
# You can think of it like a spreadsheet or SQL table, or a dict of Series objects.
# It is generally the most commonly used pandas object.

# ***********************************************************************************************************
# From dict of Series or dicts
# ***********************************************************************************************************

# The result index will be the union of the indexes of the various Series. If there are any nested dicts, these
# will be first converted to Series. If no columns are passed, the columns will be the sorted list of dict keys.

d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
     'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

print("\n df: \n")
print(df)

# The roles of index and column are similar to Series'

df1 = pd.DataFrame(d, index=['d', 'b', 'a'], columns=['two', 'three'])

print("\n df1: \n")
print(df1)

# The row and column labels can be accessed respectively by accessing the index and columns attributes:

print("\n df.index: \n")
print(df.index)
print("\n df.columns: \n")
print(df.columns)

# ***********************************************************************************************************
# From dict of ndarrays / lists
# ***********************************************************************************************************

# The ndarrays must all be the same length. If an index is passed, it must clearly also be the same length as
# the arrays. If no index is passed, the result will be range(n), where n is the array length.

# If lengths of arrays are different: "ValueError: arrays must all be same length"

d = {'one': [1., 2., 3., 4.],
     'two': [4., 3., 2., 1.]}

print("\n pd.DataFrame(d): \n")
print(pd.DataFrame(d))
print("\n pd.DataFrame(d, index=['a', 'b', 'c', 'd']): \n")
print(pd.DataFrame(d, index=['a', 'b', 'c', 'd']))

# ***********************************************************************************************************
# From structured or record array
# ***********************************************************************************************************

data = np.zeros((2,), dtype=[('A', 'i4'),('B', 'f4'),('C', 'a10')])
print(data)

# ERRE MAJD KÉSŐBB VISSZATÉREK :D
# https://docs.scipy.org/doc/numpy/user/basics.rec.html
# b1, i1, i2, i4, i8, u1, u2, u4, u8, f2, f4, f8, c8, c16, a<n> (representing bytes, ints, unsigned ints,
# 7floats, complex and fixed length strings of specified byte lengths)

# ***********************************************************************************************************
# From a list of dicts
# ***********************************************************************************************************

data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

print("\n pd.DataFrame(data2): \n")
print(pd.DataFrame(data2))

# And if I give index and column - both are optional

print("\n pd.DataFrame(data2, index=['first', 'second'], columns=['a', 'b']): \n")
print(pd.DataFrame(data2, index=['first', 'second'], columns=['a', 'b']))


# ***********************************************************************************************************
# From a dict of tuples
# ***********************************************************************************************************

# You can automatically create a multi-indexed frame by passing a tuples dictionary

df_multi = pd.DataFrame({('a', 'b'): {('A', 'B'): 1, ('A', 'C'): 2},
                         ('a', 'a'): {('A', 'C'): 3, ('A', 'B'): 4},
                         ('a', 'c'): {('A', 'B'): 5, ('A', 'C'): 6},
                         ('b', 'a'): {('A', 'C'): 7, ('A', 'B'): 8},
                         ('b', 'b'): {('A', 'D'): 9, ('A', 'B'): 10}})

print("\n df_multi: \n")
print(df_multi)

# ***********************************************************************************************************
# From a Series
# ***********************************************************************************************************

# The result will be a DataFrame with the same index as the input Series, and with one column whose name is
# the original name of the Series (only if no other column name provided).
