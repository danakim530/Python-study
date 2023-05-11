# 리스트(mutable)랑 거의 비슷
# 튜플 : 여러 값을 모아서 저장 but 값을 변경할 수 없음(immutable), 동그란 괄호 씀. 괄호 안쓰고 콤마만 써도 됨

my_tuple = ()  # 빈 튜플
print(type(my_tuple))

my_tuple = (1, 2, 3)
your_tuple = 1, 2, 3  # 괄호 없이 써도 자동으로 튜플되어 있음

# Packing(값을 묶기) vs Unpacking(묶여있는 값을 풀기)
my_tuple = 1, 2, 3  # 1,2,3 값을 튜플로 묶음 packing
num1, num2, num3 = my_tuple  # 각각 알아서 값이 들어감 unpacking
print(num1, num2, num3)

num1, num2 = num2, num1  # 값을 서로 바꿀 수 있음. 오른쪽에서 packing 되고, 왼쪽에서 unpacking 된 것
