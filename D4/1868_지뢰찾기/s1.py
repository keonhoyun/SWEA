T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    Queue = []
    ans = 0
 
    # 주변 지뢰갯수 파악하기
    for i in range(N):
        for j in range(N):
            count = 0
            # 지뢰이면 넘어가기
            if arr[i][j] == '*':
                continue
            # 지뢰가 아니면
            # 주변 탐색
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    # 지뢰 갯수만큼 숫자 기입
                    if (0 <= k < N) and (0 <= l < N) and (arr[k][l] == '*'):
                        count += 1
            arr[i][j] = count
    
    # 주변 지뢰갯수가 0이고 방문을 아직 안했다면
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0 and not visited[i][j]:
                # 방문횟수와, 방문결과 표시
                ans += 1
                visited[i][j] = 1
                # 큐에 방문 지점 넣기
                Queue.append([i, j])
                while Queue:
                    y, x = Queue.pop(0)
                    # 큐의 주변 살피기
                    for k in range(y - 1, y + 2):
                        for l in range(x - 1, x + 2):
                            # 범위가 유효하고 아직 방문을 안했다면 방문표시하기
                            # 숫자가 0인 경우만 방문하기
                            if (0 <= k < N) and (0 <= l < N) and (arr[k][l] == 0) and not visited[k][l]:
                                visited[k][l] = 1
                                Queue.append([k, l])
    # 0인 아닌 경우 방문하기
    for i in range(N):
        for j in range(N):
            if arr[i][j] in ['*', 0]:
                continue
            for k in range(i - 1, i + 2):
                for l in range(j - 1, j + 2):
                    # 주변에 갈 곳이 없으면 끝내기
                    if (0 <= k < N) and (0 <= l < N) and (arr[k][l] == 0):
                        break
                # 주변에 갈 곳이 없으면 끝내기
                if (0 <= k < N) and (0 <= l < N) and (arr[k][l] == 0):
                    break
            # 0이 아닌 숫자가 나오면 방문하기
            else:
                ans += 1
 
    print('#{} {}'.format(tc, ans))