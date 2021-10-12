num = 400
# 첫 줄의 데이터 값을 담을 리스트 구하기
arr_first = [0 for _ in range(num)]
for i in range(1, num - 1):
    arr_first[i] = arr_first[i - 1] + i

T = int(input())
for tc in range(1, T + 1):
    # pq값을 받아온다.
    p, q = map(int, input().split())
    position = [[], []]
    # 반복을 돌면서 자신보다 같거나 큰값을 찾아 좌표를 계산한다.
    for i in range(1, len(arr_first)):
        # p값 먼저 좌표 계산
        if not position[0] and p <= arr_first[i]:
            # 좌표는 리스트의 값과 차이만큼 좌표 더하고 빼기
            gab_p = arr_first[i] - p
            position[0] = [1 + gab_p, i - gab_p]
        if not position[1] and q <= arr_first[i]:
            gab_q = arr_first[i] - q
            position[1] = [1 + gab_q, i - gab_q]
        if position[0] and position[1]:
            break
    # 계산된 자표를 더한다.
    y = position[0][0] + position[1][0]
    x = position[0][1] + position[1][1]
    add_num = 0
    # 찾는 위치의 차이만큼 계산한다.
    for i in range(y - 1):
        add_num += x + i
    # 계산한 데이터를 합하여 출력
    print('#{} {}'.format(tc, arr_first[x] + add_num))