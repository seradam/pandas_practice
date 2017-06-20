import pandas as pd
import numpy as np
import savReaderWriter as spss

raw_data = spss.SavReader('jazzadatbazis.sav', returnHeader = True)
raw_data_list = list(raw_data)
data = pd.DataFrame(raw_data_list)
data = data.rename(columns=data.loc[0]).iloc[1:]
print(data)