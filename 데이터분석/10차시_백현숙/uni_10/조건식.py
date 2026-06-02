import numpy as np 
#파이썬의 list타입은 조건식 안먹는다 
#numpy랑 dataframe만 갖고 있다 

#예전의 프로그래밍 언어 - 사람들은 뭉뜽그려서 
#하나씩 하나씩 일일이 

x = [1,2,3,4,5,6,7,8,9,10]
y = []
for i in x:
    if i %2==0 :
        y.append(i)
print(y)

y = [ i for i in x  if i%2==0]
print(y)

xx = np.array(x)
print( type(x), type(xx))

print( xx % 2 == 0 )  #ndarray 데이터가 boolean이 나온다 
print()

print(  xx[ [True, True, True, True, True, False, False, False, False, False]])    


data = np.array( [-2, -4, 7, 5, 6, 11,-9, 8, 10, 15] )

print(data)
print( data >= 0 )

#print( x[x>4] )

#numpy 가 갖고 있는 기능이다 
print( data[ data >= 0 ])


print( data %2 == 0 )
print( data[ data %2 == 0] )

print( data[ [True, True, True, False, False, False, False, False, False, False] ] ) 

