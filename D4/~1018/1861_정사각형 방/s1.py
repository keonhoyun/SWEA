dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def check(r,c, road):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        
        if 0 <= nc < N and 0 <= nr < N and (room[r][c] + 1) == room[nr][nc]:
            # 조건에 맞으면 재귀
            # 바로 재귀를 돌렸더니 값이 이상하게 나옴
            temp = check(nr, nc, road + 1)
            
            # 로드값 바꾸기
            if road < temp:
                road = temp
    return road



for tc in range(1, int(input()) + 1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    # 변수값 초기화
    result = N ** 2
    ans = 1
    
    # 배열을 돌며 찾기
    for i in range(N):
        for j in range(N):
            temp = check(i, j, 1)
            if ans < temp:
                ans = temp
                result = room[i][j]
            # 값이 같으면 숫자가 작은 배열의 값
            elif ans == temp and result > room[i][j]:
                result = room[i][j]


    print('#{} {} {}'.format(tc, result, ans))


