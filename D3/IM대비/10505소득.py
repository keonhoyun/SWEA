T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    # 구할 평균 소득 구하기
    wage = sum(arr) // N
    cnt = 0
    # 평균 소득보다 작으면 cnt + 1해주기
    for i in arr:
        if i <= wage:
            cnt += 1

    print('#{} {}'.format(tc, cnt))
