T = int(input())
for tc in range(1, T + 1):
    L, U, X = map(int, input().split())
    if X > U:
        result = -1

    elif X < L:
        result = L - X
    
    else:
        result = 0

    print('#{} {}'.format(tc, result))
