#시리즈.py
import pandas as pd 
import numpy as np 
s = pd.Series([1,2,3,4, np.nan])
print(s)
print(s.isnull())

print(s.isnull().sum())
