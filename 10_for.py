# for animal in animals :
#   print(animal)

for num in [1, 2, 3]:
    print(num)

for my_str in 'dana':
    print(my_str)


# range(3) 내장 함수_____________________________________________
# type(range(3))  # 타입 찍어보면.. [0,1,2] 들어가는 것과 비슷

# range는 범위 더 쉽게 정하려고 씀.
for n in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
    print(n)

for n in range(0, 10):  # 0부터 9까지임
    print(n)


# for문 중첩(구구단 출력하기)_____________________
for j in range(2, 10):
    for i in range(1, 10):
        print('{}x{}={}'.format(j, i, j*i))
# 2x1
# 2x2
# 2x3
# ...


# 컴프리핸션_____________________________________
numbers = [1, 2, 3, 4, 5, 7, 8, 9, 10]
odd_numbers = []
for number in numbers:
    if number % 2 == 1:
        odd_numbers.append(number)  # 리스트 마지막에 요소 추가
print(odd_numbers)

# 위랑 같은 표현임. for문이랑 if문을 한 줄로 쓸 수 있음. 리스트를 만들어줌.
odd_numbers = [number for number in numbers if number % 2 == 1]
print(odd_numbers)
