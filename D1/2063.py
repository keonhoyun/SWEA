T = int(input())
# 버블정렬로 정렬
arr = list(map(int, input().split()))
for i in range(T -1, 0 , -1):
    for j in range(0, i):
        if arr[j] >= arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
# 중간값 출력
print(arr[T // 2])