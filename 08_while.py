# Loop

# While
count = 0
while count < 3:
    print('횟수: ', count)
    count += 1

# Continue: 아래 실행 안하고, 다시 조건 확인 처음부터 / break
n = 0
while n < 10:
    n += 1
    if n < 4:
        continue
    print('횟수n:', n)
    if n == 8:
        break
