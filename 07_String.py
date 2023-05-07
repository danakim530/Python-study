# 문자열(string)은 값 그리고 순서를 변경할 수 없음.

my_str = "김씨 가족"
print(my_str)
print(type(my_str))

my_str = 'dana'  # 작은 따옴표도 가능
print(my_str)

# 큰(작은) 따옴표 3개 사용하면 여러줄 저장 가능
my_str = """me 
토미
메타
"""
print(my_str)


# 문자열 Formatting(%d, %s, %f)(c언어 스타일)___________________________
my_str = 'My name is %s' % 'young chae'  # %s는 문자열 대입
print(my_str)

print('%d %d' % (1, 2))  # 정수 대입
print('%f' % 3.14)  # 실수 대입


# '{}'.format() (조금 더 파이썬스러운 방법)________________________
print('My name is %s' % 'dana')
print('My name is {}'.format('dana'))
print('{} x {} = {}'.format(2, 3, 2*3))
print('{1} x {0} = {2}'.format(2, 3, 2*3))  # 순서대로 0,1,2 주소를 가지는데 주소로 위치 지정가능

# indexing___________________________________
my_name = "dana kim"
print(my_name[3])
print(my_name[-1])  # 마이너스로 주소 지정하는 법도 있긴 함

# Slicing (잘라서 복사해옴. 원본 유지)_________________________________
my_name = 'I am dana kim'
print(my_name[5:9])
print(my_name[:3])  # 생략은 전체를 의미
print(my_name[4:])

# string.split()
