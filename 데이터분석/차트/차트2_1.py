############################################
#    seaborn 최신버전으로 업데이트 하자 
#    반드시 관리자 권한으로 
#
#    pip install seaborn --upgrade
#
#    https://seaborn.pydata.org/tutorial.html 튜토리얼 사이트 
#    https://pinkwink.kr/983  참고사이트 
#    https://wikidocs.net/45294  토닥토닥 시각화 
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

#Simple plot of linear, quadratic, and cubic curves
x = np.linspace(0, 2, 100) #0 ~ 2 까지 100개의 구간으로 나눈다 
#print(x[:10])
plt.plot(x, x, label='선형') 
plt.plot(x, x**2, label='2차')
plt.plot(x, x**3, label='3차')
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title("제목을 붙여봅시다")
plt.legend(loc="best")
plt.show()


