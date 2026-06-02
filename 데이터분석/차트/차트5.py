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

# # Pairwise bivariate
# iris = sns.load_dataset("iris")
# iris.to_csv("iris.csv", encoding="cp949")
# print( iris.head() )

# #산포도 - 서로간의 관계에 대해서 - 너무 많은  필드가 있을 경우에는 한번에 못그린다. 
# #       - 특성과 특성의 관계를 확인하기 위한 차트 
# iris = pd.read_csv("./data/iris.csv")
# print(iris.head())
# sns.pairplot(iris)
# plt.show()

# score = pd.read_excel('./data/score.xlsx')
# sns.pairplot(score)
# plt.show()

# Pairwise bivariate
iris = sns.load_dataset("iris" )
print(iris.head())
sns.pairplot(iris, hue='species') #종별특성
plt.show()

sns.pairplot(iris, height=3, vars=['sepal_width', 'sepal_length']) #종별특성
plt.show()



