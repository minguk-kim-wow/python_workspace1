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

# # Linear regression model-- plot에 추세선 그리기 
tips = sns.load_dataset("tips")
print( tips.info())
print( tips.head())

#추세선 - 1차방정식으로 선을 - 선형회귀분석 : y = ax + b 가 정답이라고 
# x = [............] y = [...............]
# 선형회귀분석  y = ax + b 가장 적절한 a와  b를 찾는다. a와 b를 찾는 알고리즘이 많다 
# 학습을 할때 전체데이터를 학습 80:20, 70:30 -> 특정데이터셋이 맞춰진다.(오버피팅),
# 노이즈 -> 잡음을 일으켜서 
# 추세선 , 추세선을 그려준다 

sns.lmplot(x="total_bill", y="tip", data=tips)
plt.show()

sns.lmplot(x="size", y="tip", data=tips, x_jitter=.15, ci=None)
#x_jitter :회귀를 피팅 한 후 데이터 복사본에 노이즈가 추가되고 산점도 모양에만 영향을줍니다.
#이산 값을 갖는 변수를 플로팅 할 때 유용 할 수 있습니다.
plt.show()

sns.lmplot(x="size", y="tip", data=tips, x_estimator=np.mean, ci=None)
plt.show()


