for tc in range(1, int(input()) + 1):
    A, B = map(int, input().split())
    ans = -1
    if A < 10 and B < 10:
        ans = A * B

    print('#{} {}'.format(tc, ans))