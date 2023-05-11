# 리스트(mutable)랑 거의 비슷
# 튜플 : 여러 값을 모아서 저장 but 값을 변경할 수 없음(immutable), 동그란 괄호 씀. 괄호 안쓰고 콤마만 써도 됨

my_tuple = ()  # 빈 튜플
print(type(my_tuple))

my_tuple = (1, 2, 3)
your_tuple = 1, 2, 3  # 괄호 없이 써도 자동으로 튜플되어 있음

# Packing(값을 묶기) vs Unpacking(묶여있는 값을 풀기)
