dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def check(r, c, road, skill):
    visited[r][c] = 1
    global ans
    if ans < road:
        ans = road

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if mountain[r][c] > mountain[nr][nc]:
                check(nr, nc, road + 1, skill)
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]
                mountain[nr][nc] = mountain[r][c] - 1
                check(nr, nc, road + 1, 0)
                mountain[nr][nc] = tmp

    visited[r][c] = 0


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    max_h = 0
    mountain = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]
    ans = 0
    visited = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                check(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))



