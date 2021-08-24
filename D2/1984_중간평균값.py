T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    # 버블정렬로 정렬하기
    for i in range(len(arr)-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
   
    ans = 0
    cnt = 0
    # 최소값과 최대값을 제외해야 하므로
    # 인덱스를 1부터 길이의 -1 까지로 잡기
    for i in range(1, len(arr)-1):
        ans += arr[i]
        cnt += 1
    # 소수 첫째자리에서 반올림
    result = round(ans/cnt)

    print('#{} {}'.format(tc, result))



