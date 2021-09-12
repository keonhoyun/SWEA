import sys
sys.stdin = open('input.txt')

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]


def BFS(arr, visited, time, start, goal):
    q = deque([start])
    while q:
        i, j = q.popleft()
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            if 0 <= ni < N and 0 <= nj < N:
                if ni == 0 and nj == 0:
                    continue

                elif visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    time[ni][nj] = time[i][j] + arr[ni][nj]
                    q.append([ni, nj])
                else:
                    if time[ni][nj] > time[i][j] + arr[ni][nj]:
                        time[ni][nj] = time[i][j] + arr[ni][nj]
                        q.append([ni, nj])





T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    time = [[0] * N for _ in range(N)]
    start, goal = [0, 0], [N - 1, N - 1]
    
    BFS(arr, visited, time, start, goal)
    answer = time[goal[0]][goal[1]]
    
    print('#{} {}'.format(tc, answer))