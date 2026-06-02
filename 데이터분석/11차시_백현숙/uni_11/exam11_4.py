#파일명 : exam11_4.py
#데이터표준화

import pandas as pd 

data = pd.read_csv('./data/auto-mpg.csv')
print(data.info())
print(data.head())

#컬럼명 변경하기 
data.columns=['mpg', 'cyl', 'disp', 'power', 'weight', 'acce', 'model']
print(data.head())

#정규화 
#(정규화하고자 하는 값 - 데이터 값들 중 최소값) / (데이터 값들 중 최대값 - 데이터 값들 중 최소값)
data['mpg2'] = (data['mpg'] - data['mpg'].min())/(data['mpg'].max()-data['mpg'].min())
print(data)

#단위환산 - 한국 단위로 환산하기 
mpg_unit = 1.60934 / 3.78541

data['kpl'] = (data['mpg'] * mpg_unit).round(2)
print( data.head() )




