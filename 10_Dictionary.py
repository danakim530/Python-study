# Dictionary : 여러개의 값을 한번에 가능. 리스트와 다르게 관련된 정보를 서로 연관시켜 놓음
# Key와 value라는 것이 있음 {key1: val1, ...}

my_dict = {}  # 빈 딕셔너리
print(type(my_dict))  # 딕셔너리 타입

my_dict[0] = 'a'  # key값이 0인 곳에 a라는 value를 넣겠다
print(my_dict)  # {0, 'a'}

my_dict['b'] = 2  # Key값이 'b'인 곳에 2라는 value를 넣겠다
print(my_dict)

my_dict['학생1'] = '호박'
my_dict['학생2'] = '김'
my_dict['학생3'] = '다나'
print(my_dict)

# 값을 가져오는 방법 : Key로 가져옴
print(my_dict['학생1'])  # 호박

# 값 지우기 : del
del my_dict[0]
print(my_dict)

# 메소드(dictionary용)_______________________________________________________
# dict.values() : 값을 뽑아오기
for std in my_dict.values():
    print(std)

# dict.keys() : 키 뽑아오기
for key in my_dict.keys():
    print(key)

# dict.items() : 키와 값을 같이 뽑아오기
for key, val in my_dict.items():
    print(key, val)
