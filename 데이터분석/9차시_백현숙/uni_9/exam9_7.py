import pandas as pd 

data1 = {'kor':90, 'eng':70, 'mat':80}
data2 = {'kor':90, 'eng':70, 'mat':80}
data3 = {'kor':90, 'eng':70, 'mat':80}
data4 = {'eng':90, 'mat':70, 'kor':80}
series1 = pd.Series( data1 )
series2 = pd.Series( data2 )
series3 = pd.Series( data3 )
series4 = pd.Series( data4 )

# result={'kor':0, 'eng':0, 'mat':0}
# result['kor'] = series1["kor"]+series2["kor"] + series3["kor"] + series4["kor"]

result1 = series1 + series2 + series3 + series4
result2 = result1/4

print("총점 ----------")
print( result1 )
print("평균 ----------")
print( result2 )
