#파일명 : exam10_8.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/auto-mpg.csv")


#value_counts 각 데이터별 고유카운트-빈도수, 발생빈도수를 카운트 한다  
print( data['model-year'].value_counts())

#평균, 최대, 최소 
print("연비평균 : ",  data['mpg'].mean())
print("연비최대 : ", data['mpg'].max())
print("연비최소 : ", data['mpg'].min())
print("연비중간 : ", data['mpg'].median())
print("연비분산 : ", data['mpg'].var())
print("연비표준편차 : ", data['mpg'].std())

print("1사분위수 : ", data['mpg'].quantile(0.25))
print("2사분위수 : ", data['mpg'].quantile(0.5))
print("3사분위수 : ", data['mpg'].quantile(0.75))

#상관계수 - 각 요소들간에 어떤 관계가 있는지 확인해보기 위한 연산 
#머신러닝 - y = ax + b 이때 a와 b를 구한다 
"""
y = 집값 
x ? - 평수, 건설업체, 지역, 지하철

상관이 있다, 상관이 없다. -1 ~ 0 ~ 1 


"""
print( data.corr() )

print( data[['mpg', 'cylinders']])
print( data[['mpg', 'cylinders']].corr() )

import matplotlib.pyplot as plt 
#차트
data.plot() 
plt.show()

