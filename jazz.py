import pandas as pd
import numpy as np
import savReaderWriter as spss
import matplotlib.pyplot as plt

# read sav file and setup colmn names:

raw_data = spss.SavReader('jazzadatbazis.sav', returnHeader=True)
raw_data_list = list(raw_data)
data = pd.DataFrame(raw_data_list)
data = data.rename(columns=data.loc[0]).iloc[1:]

# repair column names:

column_names = list(data.columns.values)
new_column_names = column_names[:]
for i in range(len(column_names)):
    new_column_names[i] = str(column_names[i])[2:-1]
helper_dict = {}
for i in range(len(column_names)):
    helper_dict[column_names[i]] = new_column_names[i]
data.rename(columns=helper_dict)

# drop off the unnecessary columns:

new_data = data[[b'ID', b'szulev', b'nem', b'szul_telepules', b'telepules', b'vegzettseg', b'zeneiskola', b'reteg', b'reteg10', b'apa_vegzettseg', b'anya_vegzettseg', b'zenesz_csaladban', b'penz', b'penz_tamogatas', b'megelhetesi_keszseg', b'zeneiskh_felkesz', b'zeneiskh_kapcsolat', b'zeneiskh_anyagi', b'fellepesbol_megelni', b'megelesi_hanyad']]

# frequency and basic statistics:

print('\nfrequencies of birth year:\n')
print(new_data[b'szulev'].value_counts())

new_data_a = new_data.copy() # I use copy because of SettingWithCopyWarning

new_data_a.loc[:, b'eletkor'] = 2017 - new_data[b'szulev']

print('\nmean of the age:\n')
print(new_data_a[b'eletkor'].mean())

print('\nmedian of the age:\n')
print(new_data_a[b'eletkor'].mode())

print('\nstandard deviation of the age:\n')
print(new_data_a[b'eletkor'].std())

print('\ncrosstab gender x education with frequencies:\n')
print(pd.crosstab(new_data_a[b'vegzettseg'], new_data_a[b'nem'], rownames=['vegzettseg'], colnames=['nem']))

# There is no built-in function for display percentage, but it is possible with lambda
# column percentage: axis=0 ; row percentage: axis=1

print('\ncrosstab gender x education with percentages:\n')
print(pd.crosstab(new_data_a[b'vegzettseg'], new_data_a[b'nem']).apply(lambda r: r/r.sum(), axis=0))

# Display frequency and percentage in one table is possible, but very complex and ugly, I don't suggest it


# new_data_a[b'nem'].plot.pie(figsize=(6, 6))
# plt.pie(new_data_a[b'nem'])
# new_data_a.plot(x=b'nem', y=b'vegzettseg', kind='scatter', xlim=[0, 0.0006])
new_data_a.plot(x=b'nem', y=b'vegzettseg', kind='pie')
plt.show()
