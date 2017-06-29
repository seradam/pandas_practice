import pandas as pd
import numpy as np
import savReaderWriter as spss
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn import datasets, linear_model

# read sav file and setup column names:

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


# gender distribution in a pie chart

new_data_a[b'nem'].value_counts().plot.pie(labels=['male', 'female'])
plt.show()

# create demographic group column

new_data_a[b'demgroup'] = np.where(new_data_a[b'eletkor']>= new_data_a[b'eletkor'].mean(), 'old', 'young')

print('\ndemograpgic group + age:\n')
print(new_data_a[[b'demgroup', b'eletkor']])

# linear regression:

# This analysis is substantively meaningless, but it is perfect for show the operation

length = 37
x = new_data_a[b'nem'].values
y = new_data_a[b'ID'].values
x = x.reshape(length, 1)
y = y.reshape(length, 1)
regr = linear_model.LinearRegression()
regr.fit(x, y)

plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()

b = [regr.coef_, regr.intercept_]

print("\nInterpretation of regression:\n The intercept is ", b[1], "which means that the average ID "
"of men is", b[1], "The b coefficient is", b[0], "which means that the average of women's ID is so less "
"than men's")