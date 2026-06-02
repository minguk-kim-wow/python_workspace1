#문자열 인덱싱과 슬라이싱 
print()
str = "Hello Python"

print( str[0] ) 
print( str[1] ) 
print( str[2] ) 
print( str[3] ) 
print( str[4] )

print( str[-1] )
print( str[-2] )
print( str[-3] )

print( str[0:5] ) #0~5번째 문자열 
print( str[:5] )
print( str[6:] )

#인덱싱을 이용한 문자열 뒤집기 
for i in range(-1, -(len(str)+1), -1):
    print(str[i], end='')
print()
print()



 