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



# logistic
tips = sns.load_dataset("tips")
tips["big_tip"] = (tips.tip / tips.total_bill) > .15
sns.lmplot(x="total_bill", y="big_tip", data=tips, 
            logistic=True, y_jitter=.03).set_axis_labels("Total Bill", "Big Tip")
plt.title("Logistic Regression of Big Tip vs. Total Bill")
plt.show()


# # lowess smoother
# tips = sns.load_dataset("tips")
# sns.lmplot(x="total_bill", y="tip", data=tips, lowess=True)
# plt.show()








