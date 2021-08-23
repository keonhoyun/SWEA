num = int(input())
# 계산할 배열 만들기
arr = [i for i in range(1, num + 1)]
result = 0
# 배열을 돌며 합산
for j in arr:
    result += j
print(result)