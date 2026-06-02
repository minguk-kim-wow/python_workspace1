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


# Pairwise bivariate
iris = sns.load_dataset("iris" )
#꽃받침의 길이와 넓이의 Joint Plot 과 Kernel Density Plot
sns.jointplot(x="sepal_width", y="sepal_length", data=iris, 
                    kind="kde").set_axis_labels("x", "y")
plt.show()

#scatter plot + histogram 
sns.jointplot(x="sepal_width", y="sepal_length", data=iris, 
                    kind="reg").set_axis_labels("x", "y")
plt.show()

