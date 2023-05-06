import random

my_int = 1  # 대소문자 구분함
print(my_int + 3)


# Data Type 자료형____________________________
# python에서는 거의 모든 형이 객체임

# Numeric 숫자형
print(type(my_int))

# String 문자열(큰, 작은 따옴표 구분 X)
print('hello')

# Boolean 자료형(참, 거짓)

# List 리스트형 (여러개를 모아서 저장, 대괄호 사용)
my_list = [1, 2, 3]
my_list2 = ['김', 'da', 'na']
print(my_list)

for list in my_list2:
    print(list)


print(random.choice(my_list2))  # 제비뽑기도 가능

my_list2.append('Meta')  # 리스트 추가하기
print(my_list2)

my_list2[0] = 'tuna'  # 하나하나 수정가능
print(my_list2)

# Tuple 튜플 (리스트와 비슷 but 안의 값을 바꿀 수 없음, 소괄호)
my_tuple = ('요거트', '이에스', '문씨')
# my_tuple[0] = '새로운 거'  # 여기 에러남

# Dictionary
my_dict = {'헤흐': '남', 'Meta': '남', '김왼손': '여'}
my_dict['헤흐'] = '여'  # 수정 가능
print(my_dict['헤흐'])


# 타입 변환하기____________________________
my_int2 = 1
print(type(my_int2))
print(float(my_int2))  # float로 바꾸기
print(str(my_int2))  # 문자열로 바꾸기
print(type(str(my_int2)))  # 문자열로 바꾸기
