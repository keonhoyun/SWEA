from itertools import combinations


def sum_combi(lst):
    tmp = []
    for i in range(len(lst)):
        if sum(lst[i]) not in tmp:
            tmp.append(sum(lst[i]))

    return tmp


for tc in range(1, int(input()) + 1):
    lst = list(map(int, input().split()))
    arr = list(combinations(lst, 3))

    tmp_lst = sorted(sum_combi(arr), reverse=True)

    print('#{} {}'.format(tc, tmp_lst[4]))





