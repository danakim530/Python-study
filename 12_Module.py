# Module : 비슷한 함수들을 모아둔 것. 파이썬에서 제공한 모듈 + 다른 사람들이 만든 모듈
# Import 해서 써야 함

# Ex. random 모듈(난수)
import random
students = ['mango', 'hee', 'nego', 'dana', 'ten']
students.append('Me')  # 리스트에 추가
print(random.choice(students))  # 모듈 안의 함수 사용! 한 개 뽑아줌
print(random.sample(students, 2))  # 여러개를 뽑아줌
print(random.sample(range(1, 45), 2))  # 랜덤 번호 추첨도 가능
print(random.randint(8, 10))  # 8부터 10 중에 랜덤 정수 하나 뽑아줌
