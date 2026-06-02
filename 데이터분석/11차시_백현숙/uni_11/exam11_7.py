#파일명 : exam11_4.py
#구간분할

import pandas as pd 
import numpy as np 

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info())
print(data.head())

#타입이 맞지 않을 경우 전환을 해서 사용해야 한다 
#현재 사용하는 파이썬 버전은 문자열 데이터라도 수치 형태면 자동으로 수치자료로 처리한다 
#파이썬 버전에 따라 다르게 동작할 수 도 있다 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.dtypes)

#잘못된 데이터를 NaN으로 먼저 바꾼다 
data['disp'].replace('?', np.nan, inplace=True)
data.dropna(subset=['disp'], axis=0, inplace=True)
data['disp'] = data['disp'].astype('float')

#범주형으로 바꾼다 
data['model'] = data['model'].astype('category')

#연속적인 값을 구간으로 나누어 비연속적인값(범주형)으로 나눈다 
#print(data['power'])

print(data['power'].isnull().sum(axis=0))
data.dropna(subset=['power'], inplace=True)

#power 필드를 구간으로 나누자 
count, bin_dividers = np.histogram(data['power'], bins=4)
print(count)
print( bin_dividers, type(bin_dividers))


#
#bin_dividers = np.array( [40, 120, 140, 200, 300])
bin_names = ["D", "C", "B", "A"]
data["grade"] = pd.cut( x=data['power'], bins=bin_dividers, 
    labels = bin_names, include_lowest=True)

print( data[:20] )
print( data["grade"].value_counts())


#onehot encoding 
#reshape 배열의 모양을 바꾼다. 차원추가  
Y_class = np.array(data['grade']).reshape(-1,1)

#사이킷런 라이브러리는 1차원 배열을 안받아 준다. 2차원배열만 받아준다 
from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder()
enc.fit(Y_class) #데이터받아서 학습을 한다. 

Y_class_onehot = enc.transform(Y_class).toarray() #원핫인코딩 작업 완료 
Y_class_recovery = np.argmax(Y_class_onehot, axis=1).reshape(-1,1)

print(Y_class_onehot)
