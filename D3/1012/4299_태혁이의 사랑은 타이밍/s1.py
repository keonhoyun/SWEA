for tc in range(1, int(input()) + 1):
    D, H, M = map(int, input().split())

    change = D * 24 * 60 + H * 60 + M
    sad = 11 * 24 * 60 + 11 * 60 + 11

    if change >= sad:
        ans = change - sad
    else:
        ans = -1

    print('#{} {}'.format(tc, ans))

