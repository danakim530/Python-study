# 함수의 종류
# 1. 내장 함수 : print() - 파이썬 기본 내장 함수
# 2. 모듈의 함수 : import해서 가져다 쓰는 함수
# 3. 사용자 정의 함수

# 함수는 한 개의 튜플을 던져준다!

def add(num1, num2):
    return num1 + num2


print(add(1, 2))


# 여러개 리턴하기
def add_multi(num1, num2):
    return num1 + num2, num1*num2


print(add_multi(1, 2))  # 튜플로 값을 반환함. 소괄호 (3,2)
my_add, my_mul = add_multi(1, 2)
