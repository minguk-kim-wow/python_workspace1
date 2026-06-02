import pandas as pd 

#인덱스가 없을 경우 값이 NaN으로 들어가서 연산이 되지 않는다 
#add 연산시 fill_value=0 옵션을 주면 대응되는 셀에 값이 없을 경우 fill_value에서 
#지정한 값으로 대신해준다 
data1 = {'kor':90, 'mat':80}
data2 = {'kor':90, 'eng':70}
data3 = {'kor':90, 'eng':70, 'mat':80}

series1 = pd.Series( data1 )
series2 = pd.Series( data2 )
series3 = pd.Series( data3 )
result1 = series1.add(series2, fill_value=0).add(series3,fill_value=0)

#보통 평균값 또는 중간값 등으로 대체한다 
print(result1)

print( series1 + 300)  #정수와의 연산도 가능하다