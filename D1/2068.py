T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
# 버블정렬로 정렬
    for i in range(len(arr) - 1, 0 , -1):
        for j in range(0, i):
            if arr[j] >= arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
# tc와 arr의 마지막요소 가져오기
    print('#{} {}'.format(tc, arr[-1]))

            