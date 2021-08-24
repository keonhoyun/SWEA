T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

# 들어갈 수 있는 단어 갯수 초기화
    word = 0
# 행 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
# 1이 나타나면 cnt +=1
            if arr[i][j] == 1:
                cnt += 1
# 0이거나 마지막열이면 그동안 cnt 갯수 검사
# K와 같으면 word +=1 아니면 cnt 초기화
            if arr[i][j] == 0 or j == N - 1:
                if cnt == K:
                    word += 1
                cnt = 0
# 열 검사
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j][i] == 0 or j == N - 1:
                if cnt == K:
                    word += 1
                cnt = 0

    print('#{} {}'.format(tc, word)) 