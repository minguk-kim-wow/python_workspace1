#C:\python_workspace\파이썬데이터분석\차트\차트1.py

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd 
from matplotlib import font_manager, rc

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

data = pd.read_excel("./data/score.xlsx")
print(data.iloc[0])
print(data.iloc[0, 1:])

# data.plot()
# plt.show()

# data.plot.bar()
# plt.show()

#산포도
data.plot.scatter("eng", "kor")
plt.show()

# data.plot.box()
# plt.show()

plt.bar(data['name'], data['kor'])
plt.show()
# plt.bar(data['name'], data['mat'])


