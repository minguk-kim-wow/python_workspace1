import pandas as pd 


#인덱스가 없을 경우 값이 NaN으로 들어가서 연산이 되지 않는다 
data1 = {'kor':90, 'mat':80} #mat 필드가 만들어지고 NaN으로 채운다
data2 = {'kor':90, 'eng':70} #eng  필드가 만들어지면서 NaN으로 채운다  (열, 키, 필드)
data3 = {'kor':90, 'eng':70, 'mat':80}  

series1 = pd.Series( data1 )
series2 = pd.Series( data2 )
series3 = pd.Series( data3 )
result1 = series1 + series2 + series3 #NaN은 값이 정해지지 않아서 여기에 연산을 수행못함 
                                      #NaN + 값을 해도 그 결과는 NaN 

print(result1)
