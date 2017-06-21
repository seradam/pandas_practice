import pandas as pd
import numpy as np
import savReaderWriter as spss

raw_data = spss.SavReader('jazzadatbazis.sav', returnHeader=True)
raw_data_list = list(raw_data)
data = pd.DataFrame(raw_data_list)
data[::1][0].str.decode("utf-8")
data = data.rename(columns=data.loc[0]).iloc[1:]
# print(type(data[0][0]))
# x = str(data[0][0])
# print(x[0])
# print(data[b'nem'])
column_names = list(data.columns.values)
# print(column_names)
new_column_names = column_names[:]
for i in range(len(column_names)):
    new_column_names[i] = str(column_names[i])[2:-1]
# print(new_column_names)
# print(column_names)
helper_dict = {}
for i in range(len(column_names)):
    helper_dict[column_names[i]] = new_column_names[i]
print(helper_dict)
data.rename(columns=helper_dict)
print(data[b'szulev'])