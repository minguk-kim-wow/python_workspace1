import pandas as pd
 
data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래', '이상민', '김수경'],
    'kor':[90, 80, 70, 70, 60, 70],
    'eng':[99, 98, 97, 46, 77, 56],
    'mat':[90, 70, 70, 60, 88, 99],
}
 
df = pd.DataFrame(data)

#새로운 필드 추가하기 
df['total'] = df.kor + df.eng + df.mat
df['avg'] = df.total/3

print(df)
