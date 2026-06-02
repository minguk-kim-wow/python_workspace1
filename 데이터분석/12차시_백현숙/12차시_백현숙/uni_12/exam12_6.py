#문자열 인덱싱은 데이터를 읽기위한 용도로만 사용된다. 
print()
str = "korea"
#str[0] ='K' - 인덱싱으로 값을 바꿀 수 없다. 
print(str)

str = 'K' + str[1:]
print(str)

str = "pyton programing"

s1 = str[0:3] + "h" + str[3:5]
s2 = str[6:12] +"m" + str[12:]
print(s1, s2)
print()
