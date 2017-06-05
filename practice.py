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
