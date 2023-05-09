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

# string.split() (띄어쓰기 단위로 잘라주는 string에 쓸 수 있는 함수, 외우지 말고 이런게 있구나~ 찾아봐서 쓸 수 있게)_________________________________
print(my_name.split())
fruit_str = '거봉 수박 포도 복숭아 망고 딸기 배 참외'
fruits = fruit_str.split()
print(fruits)

# 특정 문자 기준으로 자를 수도 있음
a = 'Life is : too : short'
print(a.split(':'))

# Docstring (큰, 작은 따옴표 세개로 주석할 수 있음. 프로그램 실행에 영향을 안 미침. 나중에 함수 설명할 때 주석으로 씀)
'''이것도 주석입니다'''


# print 옵션(end, 출력의 끝을 지정)____________________________________________
print('집단지성')  # 맨 뒤에 엔터가 기본으로 들어감
print('집단지성', end='')  # 맨 뒤의 엔터 제거
print('집단지성', end='/hello')  # 출력의 끝에 이어서 입력됨

# Escape Code(\n: 엔터, \t : 탭) 백슬래쉬!! ____________________________
print('미운코딩새끼의\n집단지성')
print('미운코딩새끼의\t집단지성')
print('미운', end='\t')  # 맨 뒤에 탭 넣기
print('코딩')
