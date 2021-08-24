T = int(input())
for tc in range(1, T + 1):
    num = int(input())
    rock_lst = list(map(int, input().split()))
    min_move = abs(rock_lst[0] - 0)
    cnt = 0
    for i in rock_lst:
        if min_move > abs(i - 0):
            min_move = abs(i - 0)
            cnt = 1
        elif min_move == abs(i - 0):
            cnt += 1

    print('#{} {} {}'.format(tc, min_move, cnt))
