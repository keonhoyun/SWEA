from itertools import permutations

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    remember = [list(map(int, input().split())) for _ in range(M)]

    lsts = list(permutations(range(1, N + 1)))

    cnt = 0
    for lst in lsts:



