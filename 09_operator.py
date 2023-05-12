# Operator 연산자
# Assign 할당 연산자
count = 1
print(count)

# 복합 할당 연산자
count += 1
count -= 1
count *= 2
count /= 3

# Arithmetic 산술 연산자 (숫자끼리)
# + - * /

# 특수 연산자
# ** : 제곱
# // : 몫
# % : 나머지
print(3**2)  # 3의 제곱
print(7/3)  # 2.333
print(7 // 3)  # 몫이 2
print(7 % 3)  # 나머지가 1

# Ex. 홀짝 구분하기
numbers = [1, 2, 3, 4, 5, 6, 7]
for number in numbers:
    if number % 2 == 1:
        print(number, "는 홀수")
    else:
        print(number, "는 짝수")


# String 연산자
print('김왼손' + 'x' + '다나')  # + : 연결하는 연산자
print('안녕하세요'+' '+'반갑습니다')
print('안녕 '*4)  # * : 문자열 반복

# Ex. 터미널 밀어버리기


def cls():
    print('\n'*100)


cls()


# Comparison 비교 연산자
# ==  !=  <  <=  >  >=  : true, false

# Logical 논리 연산자
True and False  # False
True or False  # True
not True  # False

# 예제
height = 120
age = 10
height > 140 and age > 10  # False and False라서 False

# Membership 멤버쉽 연산자 : 어떤 리스트 안에 값이 있는지 없는지 확인
# in, not in
MyList = ['dana', 'kim', 'yogurt', 'Ryu', 'mango', 'meta', 'Fire']
'dana' in MyList  # True
'mate' in MyList  # False
'dana' not in MyList  # False
