for tc in range(1, int(input()) + 1):
    N = int(input())
    dumy = []

    for _ in range(N):
        temp = int(input())
        dumy.append(temp)

    origin = sum(dumy) // N
    result = []

    for i in range(N):
        tem = abs(origin - dumy[i])
        result.append(tem)

    print('#{} {}'.format(tc, sum(result) // 2))