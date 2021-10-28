# 런타임 에러

from itertools import permutations

def check(lst, remember):
    if lst.index(remember[0]) > lst.index(remember[1]):
        return 0
    return 1



for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    remembers = [list(map(int, input().split())) for _ in range(M)]

    lsts = list(permutations(range(1, N + 1)))

    cnt = 0
    for lst in lsts:
        for remember in remembers:
            tmp = check(lst, remember)
            if not tmp:
                break
        if tmp:
            cnt += 1
    print('#{} {}'.format(tc, cnt))





