import sys
sys.stdin = open('input.txt')

from collections import deque

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def BFS(arr, visited, time, start, goal):
    # 시작점 넣기
    q = deque([start])
    # 큐가 있을 동안 반복
    while q:
        # 시작점 꺼내오기
        i, j = q.popleft()

        # 델타를 활용하여 방향 탐색
        for k in range(4):
            ni = i + di[k]
            nj = j + dj[k]

            # 만약 델타를 적용한 좌표값이 유효하면
            if 0 <= ni < N and 0 <= nj < N:

                # 해당 좌표값이 0이면 계속하기
                if ni == 0 and nj == 0:
                    continue
                
                # 아직 방문하지 않았다면
                elif visited[ni][nj] == 0:
                    # 방문표시
                    visited[ni][nj] = 1

                    # 시간표시
                    time[ni][nj] = time[i][j] + arr[ni][nj]

                    # 큐에 담기
                    q.append([ni, nj])

                # 만약 시간이 최소값이 나오면 교체하기
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