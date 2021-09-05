import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 행렬의 크기 3~50
    arr = [list(input()) for _ in range(N)]
    minV = N * M

    w_cnt = 0
    for w in range(0, N - 2):  # 화이트
        for k in range(0, M):
            if arr[w][k] != 'W':
                w_cnt += 1

        b_cnt = 0
        for b in range(w + 1, N - 1):  # 블루
            for k in range(0, M):
                if arr[b][k] != 'B':
                    b_cnt += 1

            r_cnt = 0
            for r in range(b + 1, N):  # 레드
                for k in range(0, M):
                    if arr[r][k] != 'R':
                        r_cnt += 1

            cnt = w_cnt + b_cnt + r_cnt
            if minV > cnt:
                minV = cnt

    print(f'#{tc} {minV}')