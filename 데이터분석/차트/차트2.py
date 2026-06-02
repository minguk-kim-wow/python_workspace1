import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
#font_manager - 폰트를 폰트객체화 
#rc - 폰트를 지정할 영역 (차트영역)

##절대 경로로 폰트 설정하기
# font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/HYDNKM.TTF").get_name() 

##상대 경로로 폰트 설정하기
font_name = font_manager.FontProperties(fname="./fonts/HYBDAM.TTF").get_name()
rc('font', family=font_name)

##사용가능한 폰트 알아보기#### 
import matplotlib.font_manager as fm
font_list = [font.name for font in fm.fontManager.ttflist]
#print(font_list)

##폰트 설정하는 다른방법####
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family']='Malgun Gothic'

#https://seaborn.pydata.org/tutorial.html

#Simple plot of linear, quadratic, and cubic curves
x = np.linspace(0, 2, 100) #0 ~ 2 까지 100개의 구간으로 나눈다 
print(x[:10])
plt.plot(x, x, label='선형', color='g') 
plt.plot(x, x**2, label='2차', color='r')
plt.plot(x, x**3, label='3차', color='b')
plt.xlabel('x 축')
plt.ylabel('y 축')
plt.title("제목을 붙여봅시다")
plt.legend(loc="best") #범주 출력위치,  범주는 plot함수내에서 label 
plt.show()


