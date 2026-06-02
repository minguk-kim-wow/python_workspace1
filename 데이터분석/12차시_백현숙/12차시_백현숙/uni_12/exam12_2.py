
value1 = input("정수를 입력하세요 ")
value2 = input("정수를 입력하세요 ")

#print( value1.isdigit() )
if value1.isdecimal() and  value2.isdecimal():
    result = value1 + value2 
    print("결과는 ", result, " 입니다 ")

    #위의 코드 수정하기 
    result2 = int(value1) + int(value2)
    print("결과는 ", result2, " 입니다 ")
else:
    print("정수를 입력하지 않아서 연산에 실패했습니다")



 