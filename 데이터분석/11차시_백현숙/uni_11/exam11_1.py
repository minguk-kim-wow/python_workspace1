#파일명 : exam11_1.py

import pandas as pd 

#header가 3번째 줄에 있음 
data = pd.read_csv("./data/data.csv")

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

print( data.info() )
print( data.head() )


#누락된 데이터가 있는지 확인하자. 
print( data['height'].value_counts(dropna=False))
print( data['height'].isnull()) #NaN이면 True, 아니면 False반환
print( data['height'].notnull()) #Nan일때 False 아니면 True 반환 


#null값인것에 대한 개수 확인 
print( data['height'].isnull().sum(axis=0))
print( data['weight'].isnull().sum(axis=0))

#어떤 열중에서, 행에서 기본으로 적어도 이정도의 데이터의 개수는 유지해줘라 
#nan 아닌값이 thresh개 못가진 열이나 행을 삭제 
#한 열이 적어도 NaN 이 아닌 데이터가 28개 존재해야 한다 
data_thresh = data.dropna(axis=1, thresh=28)
#inplace=True 를 줬으면 data 에 있는 값들이 삭제되지만 그 옵션을 생략해서 
#삭제된 데이터를 반환한다 
print( data_thresh)

#한행에 필드가 3개임, 3개중 2개가 적어도 NaN이 아니어야 한다  
data_thresh = data.dropna(axis=1, thresh=2)
print( data_thresh)


#합계
print ( data['height'].sum() )

print("데이터 개수")
print(data.shape)
data2 = data.dropna(subset=['height'], how='any', axis=0)
print("삭제후 데이터개수")
print(data2.shape)

data2 = data.dropna(subset=['weight'], how='any', axis=0)
print("삭제후 데이터개수")
print(data2.shape)

data.dropna(subset=['height','weight'], how='any', axis=0, inplace=True)
print( data )
#인덱스 다시 부여
data = data.reset_index(drop=True)
print(data)