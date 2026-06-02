#문자열 관련 함수들

s="I like star red star yello star blue star"
words = s.split()
print( words )

s1 = "소나무,전나무,오동나무,사시나무,향나무"
woods = s1.split(",")
print(woods)

#문자열의 길이
print( "문자열 길이 : ", len(s) )

#특정 문자의 개수 
print ("star 개수 : ", s.count("star"))

#star 의 위치 
print("star 첫번째 위치 : ", s.index("star"))
#모든 star 찾기 

print("star 위치")
key = "star"
pos=0
while  s.count(key, pos)!=0:
    pos = s.index(key, pos)
    pos = pos + len(key) #단어길이만큼 다음 위치로 이동한다
    print(pos)

print("소문자 대문자 체인지")
s2 = s.upper()
print(s2)

s1 = s2.lower()
print(s1)

#문자열 대체하기 
#star 을 moon으로 대체 
s = s.replace("star", "moon")
print(s)

#공백제거
s = "   space remove   "
print( "*" + s + "*")
print( "*" + s.lstrip() + "*")
print( "*" + s.rstrip() + "*")
print( "*" + s.strip() + "*")

#문자열 결합 
s = ",".join(["apple", "orange", "banana", "mango", "cherry"])
print(s)

s = " ".join(["apple", "orange", "banana", "mango", "cherry"])
print(s)


