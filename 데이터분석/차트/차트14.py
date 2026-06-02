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

##상대 경로로 폰트 설정하기
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

titanic = sns.load_dataset("titanic")
print( titanic.head(10))


#생존자를 대상으로 pivot 테이블을 만든다.  빈도수 세기, 분할표 - 범주형 데이터의 경우에 
#카운트를 세서 처리해야한다. 여자중에 산사람 몇명, 죽은사람 몇명 
titanic_size = titanic.pivot_table(
    index="class", columns="sex", aggfunc="size")
print(titanic_size)


sns.heatmap(titanic_size, cmap=sns.light_palette("gray", as_cmap=True), 
annot=True, fmt="d")
plt.title("Heatmap")
plt.show()


flights = sns.load_dataset('flights')
print( flights.head(10))

#분할표, 피봇테이블 
flights_passengers = flights.pivot("month", "year", "passengers")
print( flights_passengers.head(10))

plt.title("연도, 월 별 승객수에 대한 Heatmap")
sns.heatmap(flights_passengers, annot=True, fmt="d", linewidths=1)
plt.show()
