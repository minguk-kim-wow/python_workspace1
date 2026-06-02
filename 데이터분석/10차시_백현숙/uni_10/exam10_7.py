
#파일명 : exam10_7.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/auto-mpg.csv")

data2 = data[:10] #데이터 10개만 자름 
print(data2)

print("조건식 적용하기 ")
#실린더 개수 4개 짜리만 
print( data2[data.cylinders==4]  )

#실린더 개수가 8개짜리만 확인 
#data 프레임에 있는 cylinder ==8 조건을 가지고 모든 데이터를 비교해서 True 또는 False집합이 온다 

print( data2.cylinders==8 )

print( data2[[True, False, True, False, True, False, True, True, True, True]]  )


#연비가 27 이상만   data.mpg, data['mpg']
print( data[data.mpg>=27] )

#모델 연도가 70년이고 연비가 27이상만, -(하이픈) 때문데 data.model-year 는 안된다. 
#아래처럼 하던지 아니면 컬럼명을 수정해야 한다 
print ( data[data['model-year']==70])

#두가지 조건을 동시에 주고 싶을때 - 에러발생 이렇게 못쓴다 
#print( data[ data['model-year']==70 or data['mpg']>=25 ])
#ValueError: The truth value of a Series is ambiguous. Use a.empty, a.bool(), a.item(), a.any() or a.all().

#두가지 조건을 동시에 주고 싶을때 
import numpy as np 
print(data [np.logical_and(data['model-year']==70, data['mpg']>=25)])

#문제1. 모델이 70년대인것만 카운트 - 데이터 개수 
print( data[data['model-year']==70]['mpg'].count())

#문제2. 모델이 80년도인것에 대해서 연비  평균을 구하시오 
print ( data[data['model-year']==80]['mpg'].mean())
