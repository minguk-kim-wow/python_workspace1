file = open("./data/data.txt", encoding="utf8")
data = file.read()
print(data)
file.close()

#토큰분리하기 
tokens = data.split()
print( len(tokens))

#Too 와 Time 단어가 각각 몇번 등장했는지 
print("Too 개수 : ", data.count("Too"))
print("Time 개수 : ", data.count("Time"))

#who 등장 위치를 배열로 
key = "who"
pos = 0
positions = list() 
while data.count(key, pos)!=0:
    pos = data.index(key, pos)
    positions.append(pos)
    pos = pos + len(key)
print(positions)

#모든 토큰을 대문자로 바꾸어서 토큰의 번호, 대문자로 전환한 토큰 출력하기 
for i, token in enumerate(tokens):
    print(i, token.upper() )