# pythontutor.com 참고하기
# 내가 코드를 작성하는 것보다 다른 사람이 내 코드를 읽는 경우가 더 많다.
# PEP8(코딩컨벤션) : 파이썬 쓸 때 지키면 협업시 좋다. 파이썬 공식 홈페이지에 있다.

# 대소문자
str.isupper()  # true, false 출력
str.upper()  # 대문자로
str.lower()  # 소문자로

# 정수화 int()
# 문자화 str()

# 두 정수 중 큰 수 뱉기
max(A, B)

# 더하기(곱하기는 내장함수 없음)
sum(a, b)

# 길이 len()

# 문자열 합치기 join() - 더하기 안해도 됨. 한 줄로 끝남
words = ["안녕", "나는", "다나"]
result = ' '.join(words)
print(result)

# 문자열 합치기 append()

# if, if not

# 문자열 안에 특정 문자열 있는지 확인
# if str1 in str2 / not in도 가능!

#  return 1 if str1 in str2 else 0 이런 순서로도 가능!

# range(10,1,-1) 10부터 1까지 -1되는 수 차례로 10,9,8,7,,,

# for i in arr // arr배열에 있는 원소들 직접
# for i in range(0,len(arr)): arr[i] 어쩌구 안해도 됨.

# 정렬: 오름차순, 내림차순, 가나다순 등..
list.sort()  # 리스트 자체를 정렬
new_list = list.sorted()  # 새롭게 정렬된 리스트 자체를 반환

#
