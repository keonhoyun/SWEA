T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    matrix[N // 2 - 1][N // 2 - 1:N // 2 + 1] = [2, 1]
    matrix[N // 2][N // 2 - 1:N // 2 + 1] = [1, 2]
    Go = []
    for _ in range(M):
        Go += [list(map(int, input().split()))]

    dxy = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for item in Go:
        x, y, c = item
        matrix[y - 1][x - 1] = c

        for dy, dx in dxy:
            ny, nx = y - 1 + dy, x - 1 + dx
            change = [[ny, nx]]

            while -1 < nx < N and -1 < ny < N and matrix[ny][nx] != 0 and c != matrix[ny][nx]:
                ny, nx = ny + dy, nx + dx
                change.append([ny, nx])

            if len(change) > 1 and -1 < nx < N and -1 < ny < N and matrix[ny][nx] != 0:
                for i, j in change:
                    matrix[i][j] = c

    b_cnt = 0
    w_cnt = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                b_cnt += 1
            elif matrix[i][j] == 2:
                w_cnt += 1
    print('#{} {} {}'.format(tc, b_cnt, w_cnt))


# T = int(input())
# for tc in range(1, T+1):
#     n, m = map(int, input().split())
#     arrs = [list([0]*(n+2)) for _ in range(n+2)]
#     arrs[n//2][n//2+1] = arrs[n//2+1][n//2] = 1
#     arrs[n//2+1][n//2+1] = arrs[n//2][n//2] = -1
#     for i in range(m):
#         x, y, c = map(int, input().split())
#         if c == 2:
#             c = -1
#         arrs[y][x] = c
#         for j in [-1, 0, 1]:
#             for k in [-1, 0, 1]:
#                 re = 1
#                 while arrs[y+j*re][x+k*re] == c*(-1):
#                     re += 1
#                     if arrs[y+j*re][x+k*re] == c:
#                         for l in range(1, re):
#                             arrs[y+j*l][x+k*l] = c
#     B = W = 0
#     for arr in arrs:
#         for x in arr:
#             if x == 1:
#                 B += 1
#             elif x == -1:
#                 W += 1
#     print(f'#{tc}', B, W)
