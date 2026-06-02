import pandas as pd

data = {
    'class':[1,1,1,2,2,2,3,3,3,4,4,4],
    'name':['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'],
    'kor':[90, 80, 80, 70, 70, 70, 60, 60, 75, 90, 99, 93],
    'eng':[80, 70, 60, 70, 50, 80, 90, 80, 70, 80, 99, 93],
}

df = pd.DataFrame(data)
print(df)

#특정행에 필터링을 건다 
print( df['class']==1)

print("1반")
print( df[ df['class']==1] )

print("\n2반")
print( df[ df['class']==2] )

print("\n3반")
print( df[ df['class']==3] )


#우선 3반 학생들 데이터를 추출해서 
df3 = df[df['class']==3] 
print("3반의 국어평균 : ", df3['kor'].mean())


df4 = df[df['class']==4] 
print("4반의 국어평균 : ", df4['kor'].mean())
print("4반의 영어평균 : ", df4['eng'].mean())

#각반에서 국어성적이 90이상인 사람만 
#print( df[df['kor']>=90 and df['eng']>=90])

#1.된다   2.안된다 

import numpy as np
print( np.logical_and(df['kor']>=90,  df['eng']>=90) )

result = df[ np.logical_and(df['kor']>=90,  df['eng']>=90) ]
print(result)
