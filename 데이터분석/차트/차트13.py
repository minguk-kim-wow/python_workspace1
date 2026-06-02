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
font_name = font_manager.FontProperties(fname="./fonts/HYBDAM.TTF").get_name()
rc('font', family=font_name)



#Condition on other variables
tips = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", hue="smoker", data=tips,
          markers=["o", "x"], palette="Set1")

sns.lmplot(x="total_bill", y="tip", hue="smoker",
          col="time", row="sex", data=tips)
plt.show()


#Control shape and size of plot
tips = sns.load_dataset("tips")
sns.lmplot(x="total_bill", y="tip", col="day", data=tips, col_wrap=2, height=3)
#sns.lmplot(x="total_bill", y="tip", col="day", data=tips, aspect=.5)
plt.show()


# Plotting regression in other contexts
tips = sns.load_dataset("tips")
sns.jointplot(x="total_bill", y="tip", data=tips, kind="reg")
sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
            size=5, aspect=.8, kind="reg")
sns.pairplot(tips, x_vars=["total_bill", "size"], y_vars=["tip"],
            hue="smoker", size=5, aspect=.8, kind="reg")
plt.show()





