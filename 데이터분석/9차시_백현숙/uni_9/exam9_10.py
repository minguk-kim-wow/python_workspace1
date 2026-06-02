import pandas as pd 

data1 = {'kor':90, 'eng':70, 'mat':80}
data2 = {'kor':99, 'eng':75, 'mat':70}
data3 = {'kor':85, 'eng':80, 'mat':60}

data = pd.DataFrame()
data = data.append( data1 , ignore_index=True)
data = data.append( data2 , ignore_index=True)
data = data.append( data3 , ignore_index=True)

#각 필드값들을 더하여 새로 작성한 필드에 저장함 
data['total'] = data.kor + data.eng + data.mat
data['avg'] = data.total/3 

print(data)
