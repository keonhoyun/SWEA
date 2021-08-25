T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = 0
# 2071과 접근 동일
# 홀수인 경우만 더해주기
    for i in arr:
        if i % 2:
            ans += i
    print('#{} {}'.format(tc, ans))
