T = int(input())
for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    if a == b:
        result = c
    else:
        if a == c:
            result = b
        else:
            result = a
    print('#{} {}'.format(tc, result))
        