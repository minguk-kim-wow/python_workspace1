############################################
#    seaborn 최신버전으로 업데이트 하자 
#    반드시 관리자 권한으로 
#
#    pip install seaborn --upgrade
#
#    https://seaborn.pydata.org/tutorial.html 튜토리얼 사이트 
#    https://pinkwink.kr/983  참고사이트 
############################################


import numpy as np
import pandas as pd

######################################
import seaborn as sns #matplotlib 보다 먼저 import 되어야 한다 
#######################################
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc


#seaborn 컬러 지정하기 
#seaborn을 이용하여 디자인을 입히자 
sns.set(color_codes=True) #먼저 지정해야 한글이 안깨진다 
sns.set_style('darkgrid') #배경 설정하기 {darkgrid, whitegrid, dark, white, ticks}

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

#y= ax+b 
#y = ax1 + bx2 + cx3 ....  x가 많다
# Scatter plot-산포도 
mean, cov = [5, 10], [(1, .5), (.5, 1)]  
#다변수 정규분포 , 평균값과  공분산행렬 
data = np.random.multivariate_normal(mean, cov, 200)
print(data[:5])

#seaborn 은  numpy타입이 아니라 dataframe을 사용
data_frame = pd.DataFrame(data, columns=["x", "y"])
print(data_frame.head())

sns.jointplot(x="x", y="y", data=data_frame, kind="reg").set_axis_labels("x", "y")
plt.suptitle("Joint Plot of Two Variables with Bivariate and Univariate Graphs")
plt.show()
