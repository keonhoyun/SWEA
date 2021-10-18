def search(l, r):
    global result
    m = (l + r) // 2    # 중간값 설정
    if l > r:           # 만약 왼쪽이 오른쪽 보다 커지면
        result = l      # result 를 왼쪽에 맞추고 return
        return

    cnt = 0
    for i in range(N):      # 모든 심사대 순회
        cnt += m // T[i]    # 현재 m 에 대하여 몇명을 심사할 수 있는지 cnt 에 저장

    if cnt >= M:            # M 명 이상 할 수 있으면
        search(l, m - 1)    # 중간값보다 작은 범위로 다시 재귀

    else:                   # M 명 미만으로 할 수 있으면
        search(m + 1, r)    # 중간값보다 큰 범위로 다시 재귀


for test_case in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    T = [int(input()) for _ in range(N)]
    result = 0

    search(min(T), max(T) * M)

    print('#{} {}'.format(test_case, result))
