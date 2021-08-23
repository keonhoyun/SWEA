number = int(input())
for i in range(1, number + 1):
# 나머지가 0이면 출력하기
    if number % i == 0:        
        print(i, end = ' ')