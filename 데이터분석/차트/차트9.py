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


# Box plots
tips = sns.load_dataset("tips")
sns.boxplot(x="day", y="total_bill", hue="time", data=tips)
print(tips.day.unique())#일요일, 토요일, 목요일, 금요일 4일분만 있음 
plt.show()


#범주형 변수와 수(치)형 변수간 관계 시각화-boxplot와 유사
sns.catplot(x="time", y="total_bill", hue="smoker",
               col="day", data=tips, kind="box", height=4, aspect=.5)
plt.show()


sns.catplot(x="time", y="total_bill", hue="smoker",
               col="day", data=tips,  kind="violin", height=4, aspect=.5)
plt.show()


