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

#Histogram
x = np.random.normal(size=1000) #정규분초를 이루도록 1000개 무작위로 
sns.displot(x, bins=20, #구간개수
                kde=True,  #커널밀도
                rug=False, #러그 표시여부 - 데이터에 선분이 보인다 
                label="히스토그램 w/o Density")
sns.utils.axlabel("Value", "Frequency")

plt.title("Histogram of a Random Sample from a Normal Distribution")
plt.legend()
plt.show()


