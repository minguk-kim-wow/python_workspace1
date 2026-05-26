# 1. 사용자로부터 두 개의 정수 입력 받기
# 정수 계산을 위해 int() 형태로 변환합니다. (소수점 입력 시 에러 발생)
num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

print("-" * 30)
print("     [ 정수 사칙연산 결과 ]")
print("-" * 30)

# 2. 사칙연산 수행 및 출력

# 더하기
print(f"➕ 더하기 ({num1} + {num2}) = {num1 + num2}")

# 빼기
print(f"➖ 빼기 ({num1} - {num2}) = {num1 - num2}")

# 곱하기
print(f"✖️ 곱하기 ({num1} × {num2}) = {num1 * num2}")

# 나누기 (0으로 나누는 경우 예외 처리)
if num2 != 0:
    # 일반 나눗셈 (결과는 소수점으로 나올 수 있음)
    print(f"➗ 나눗셈 ({num1} ÷ {num2}) = {num1 / num2}")
    # [정수용 추가 학습] 몫과 나머지
    print(f"몫     ({num1} // {num2}) = {num1 // num2}")
    print(f"나머지 ({num1} % {num2}) = {num1 % num2}")
else:
    print("➗ 나누기 계열: 0으로 나눌 수 없습니다.")

print("-" * 30)