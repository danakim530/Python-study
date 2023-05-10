# immutable 값을 변경 X (문자열)
# mutable 값을 변경 O (리스트)

my_list = []  # 빈 리스트
print(my_list)
print(type(my_list))

my_num = [1, 2, 3]
std = ['dana', 'gana', 'maba']

# 나중에 추가하기 (append()는 리스트 함수임)
std.append('tomi')
print(std)

animals = []  # 빈리스트
print(animals)
animals.append('코알라')
animals.append('바다소')
animals.append('땅다람쥐')
animals.append('하이에나')
animals.append('고양이')
print(animals)

# indexing, delete, slicing
print(animals[3])
del animals[3]  # 지워버리기
print(animals)
print(animals[1:3])  # index 1부터 3까지 인데 왜(?)

# 메소드 sort()
animals.sort()  # 가나다 순으로 정렬
print(animals)

# 메소드 count()
print(animals.count('바다소'))  # 바다소가 몇 명이 있냐

# 길이 출력
print(len(animals))
