#파일명 : exam10_1.py

import pandas as pd 

#상대경로 지정 
data = pd.read_csv("./data/score.csv")
data = pd.read_csv(r".\data\score.csv")
data = pd.read_csv(".\\data\\score.csv")

#글꼴이 영문폰트의 경우에는 \ 한글폰트 의 경우에는 원화표시로 
data = pd.read_csv('C:\\데이터분석\\데이터분석\\10차시_백현숙\\uni_10\\data\\score.csv')
data1 = pd.read_csv(r'C:\데이터분석\데이터분석\10차시_백현숙\uni_10\data\score.csv')
data2 = pd.read_csv('C:/데이터분석/데이터분석/10차시_백현숙/uni_10/data/score.csv')

print(data)
print(data1)
print(data2)

print("컬럼명 : ", data.columns)
print("인덱스 : ", data.index)

#총점, 평균 구하기 
data['total'] = data['kor'] + data['eng']+data['mat']
data['avg'] = data['total']/3

print( data )
