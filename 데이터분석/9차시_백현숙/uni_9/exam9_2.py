import pandas as pd

#dict 타입의 데이터를 정의한다
#dict타입은 키와 값 쌍으로 이루어진다. 
#특정키값에 데이터를 여러개 넣을 경우에 키:리스트 형태로 저장할 수 있다  
data = {
    'name':['홍길동', '임꺽정', '장길산', '홍경래'],
    'kor':[90, 80, 70, 70],
    'eng':[99, 98, 97, 46],
    'mat':[90, 70, 70, 60],
}
 
df = pd.DataFrame(data)
print("타입 : ", type(df))
print(df)