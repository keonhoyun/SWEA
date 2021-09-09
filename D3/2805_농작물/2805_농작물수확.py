import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    ans = 0
    center = int(N // 2)
    for i in range(N):
        ans += int(arr[center][i])

    for i in range(1, center + 1):
        for j in range(i, N - i):
            ans += int(arr[center - i][j])
            ans += int(arr[center + i][j])

    print('#{} {}'.format(tc, ans))
