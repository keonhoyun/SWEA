di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def work(r, c, road, skill):
    global ans
    if road > ans:
        ans = road

    visited[r][c] = 1

    for i in range(4):
        nr = r + di[i]
        nc = c + dj[i]

        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if mountain[r][c] > mountain[nr][nc]:
                work(nr, nc, road + 1, skill)
            elif skill and mountain[r][c] > mountain[nr][nc] - K:
                tmp = mountain[nr][nc]
                mountain[nr][nc] = mountain[nr][nc] - 1
                work(nr, nc, road + 1, 0)
                mountain[nr][nc] = tmp
    visited[r][c] = 0




for tc in range(1, 2):
    N, K = map(int, input().split())
    mountain = [list(map(int, input().split())) for _ in range(N)]
    max_h = 0

    for i in range(N):
        for j in range(N):
            if max_h < mountain[i][j]:
                max_h = mountain[i][j]

    visited = [[0] * N for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            if mountain[i][j] == max_h:
                work(i, j, 1, 1)

    print('#{} {}'.format(tc, ans))
















# def check(arr):
#     global start
#     ans = []
#     cnt = 1
#     ni, nj = start[0], start[1]
#     for k in range(4):
#         if 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N and arr[ni + di[k]][nj + dj[k]] > arr[ni][nj]:
#             while 0 <= ni + di[k] < N and 0 <= nj + dj[k] < N and arr[ni + di[k]][nj + dj[k]] > arr[ni][nj] and arr[ni][nj] != 9:
#                 cnt += 1
#                 ni = ni + di[k]
#                 nj = nj + dj[k]
#             ans.append(cnt)
#     return max(ans)
#
# for tc in range(1, 2):
#     N, K = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 1:
#                 start = [i, j]
#
#     result = []
#     for i in range(N):
#         for j in range(N):
#             if arr[i][j] == 9:
#                 continue
#             else:
#                 arr[i][j] = arr[i][j] - K
#                 result.append(check(arr))
#                 arr[i][j] = arr[i][j] + K
#
#     print(result)



