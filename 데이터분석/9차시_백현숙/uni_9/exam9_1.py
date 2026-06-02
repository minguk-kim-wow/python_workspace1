import pandas as pd

#list를 사용하여 Series 만들기
data = [10, 20, 30, 40, 50]

series = pd.Series(data)
print(type(series)) 
print(series)

#직접 index 를 부여해보기 dict -> Series 
data2 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
series2 = pd.Series(data2)
print(series2)


#인덱싱, 슬라이싱 
print( data[0], data[1], data[3]) #인덱싱 
print( data[0:3]) #슬라이싱 

#numpy 도 pandas도 슬라이싱을 제공하고 있다 
print( series[1:4]) 
print( series2['a':'d']) 


#이 방법은 파이썬에 없는데 판다스하고 넘파이만 지원한다
print( series2[['c', 'b', 'a']])

print( "합계 : ", series.sum() ) 
print( "평균 : ", series.mean() ) 
print( "표준편차 : ", series.std() )
print( "최대값 : ", series.max() )
print( "최소값 : ", series.max() )
print( "중간값 : ", series.median() )




