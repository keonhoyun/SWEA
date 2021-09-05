import sys
sys.stdin = open('input_1244.txt')
#
T = int(input())
for tc in range(1, T + 1):
    bonus, N = map(int, input().split())
    bonus_lst = list(map(int, str(bonus)))
    maxV = bonus_lst[-1]
    for i in range(len(bonus_lst) - 1, -1, -1):
        if maxV < bonus_lst[i]:
            maxV = bonus_lst[i]
    Idx = bonus_lst.index(maxV)
    minIdx = bonus_lst.index(min(bonus_lst))

    if N == 1:
        if Idx != 0:
            bonus_lst[0], bonus_lst[Idx] = bonus_lst[Idx], bonus_lst[0]
        else:



    if N > 1:







