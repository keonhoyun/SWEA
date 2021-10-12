# import sys
# sys.stdin = open('input.txt')

# .:평지 / *: 벽 / # 강철벽 / - 물 / ^ 위로 보는 전차 / V 아래보는 전차 / < 왼쪽 전차 / > 오른쪽 전차
# U 방향 위쪽으로 / D 방향 아래쪽으로 / L 방향 왼쪽으로 / R 방향 오른쪽으로 / S 포탄발사

# dir = {
#     'U': 1,
#     'D': 2,
#     'L': 3,
#     'R': 4,
#     'S': 5
# }
#
# for _ in range(98):
#     tc = int(input())
#     H, W = map(int, input().split())
#     matrix = [list(input()) for _ in range(H)]
#     N = int(input())
#     command = input()
#
#     for i in range(N):
#         now = dir[command[i]]
#         for j in range(H):
#             for k in range(W):
#                 if matrix[j][k] == '.':
#                     continue


di = [-1, 0, 1, 0]      # 상우하좌
dj = [0, 1, 0, -1]
idx = {'^': 0, '>': 1, 'v': 2, '<': 3}  # 델타탐색을 위한 인덱스
direct = {'U': '^', 'D': 'v', 'R': '>', 'L': '<'}  # 명령어를 현재 방향으로 변환하기 위함
 
# 함수 정의 - 인덱스 범위 내에 있는지 확인
def is_able(i, j):
    return 0 <= i < H and 0 <= j < W
 
def ctrl(command):
    global curr     # 현재 전차의 위치
    i, j = curr[0], curr[1]     # 전차 위치 인덱스
    curr_direct = field[curr[0]][curr[1]]     # 현재 전차의 방향
 
    if command in direct:      # 방향을 이동해봅시다.
        new_direct = direct.get(command)    # 새로운 전차의 방향
        k = idx.get(new_direct)  # 새로운 전차의 방향에 따른 델타탐색 방향 지정
        field[i][j] = new_direct # 방향 바꿔주기
        ni, nj = i + di[k], j + dj[k]
        if is_able(ni, nj):
            if field[ni][nj] == '.':          # 만약 평지라면
                field[i][j] = '.'             # 현재 위치를 평지로 바꿔주고
                field[ni][nj] = new_direct    # 새로운 방향을 다음 위치에 삽입
                curr = [ni, nj]               # 현재위치를 갱신
 
 
    else:      # 포탄 발사!!
        k = idx.get(curr_direct)  # 현재 전차의 방향에 따른 델타탐색 방향 지정
        ni, nj = i + di[k], j + dj[k]
        while is_able(ni, nj) and field[ni][nj] != '#':       # 인덱스 범위 내에 있고, #를 만날 때까지 포탄 이동
            if field[ni][nj] == '*':      # 만약 벽돌로 만들어진 벽이라면
                field[ni][nj] = '.'      # 평지화
                break
            ni, nj = ni + di[k], nj + dj[k]
 
T = int(input())
for tc in range(1, T+1):
    H, W = map(int, input().split())        # 맵의 높이, 넓이
    field = [list(input()) for _ in range(H)]
    N = int(input())        # 사용자의 입력 개수
    commands = input()      # 사용자의 입력(명령어)
 
    # 현재 전차의 위치 파악
    for i in range(H):
        for j in range(W):
            if field[i][j] in idx:
                curr = [i, j]       # 배열에 위치 인덱스를 담아놓는다.
                break
 
    for command in commands:
        ctrl(command)
 
    print('#{}'.format(tc), end=' ')
    for m in field:
        print(''.join(m))





# T = int(input())
 
 
# def shoot(i, j, dir):
#     if dir == '^':
#         for row in range(i-1, -1, -1):
#             if game_map[row][j] == '*':
#                 game_map[row][j] = '.'
#                 return
#             elif game_map[row][j] == '#':
#                 return
#     elif dir == 'v':
#         for row in range(i+1, H):
#             if game_map[row][j] == '*':
#                 game_map[row][j] = '.'
#                 return
#             elif game_map[row][j] == '#':
#                 return
#     elif dir == '>':
#         for col in range(j+1, W):
#             if game_map[i][col] == '*':
#                 game_map[i][col] = '.'
#                 return
#             elif game_map[i][col] == '#':
#                 return
#     elif dir == '<':
#         for col in range(j-1, -1, -1):
#             if game_map[i][col] == '*':
#                 game_map[i][col] = '.'
#                 return
#             elif game_map[i][col] == '#':
#                 return
 
 
# for tc in range(1, T+1):
#     H, W = map(int, input().split())
#     game_map = [list(input()) for _ in range(H)]
#     N = int(input())
#     S = list(input())
#     di = {
#         'U': (-1, 0, '^'),
#         'D': (1, 0, 'v'),
#         'L': (0, -1, '<'),
#         'R': (0, 1, '>'),
#         'S': (0, 0)
#     }
#     start = ()
#     direction = ''
 
#     move_string = '^>v<'
 
#     flag = False
#     for i in range(H):
#         for j in range(W):
#             if game_map[i][j] in move_string:
#                 start = (i, j)
#                 direction = game_map[i][j]
#                 flag = True
#                 break
#         if flag:
#             break
 
#     while S:
#         order = S.pop(0)
#         move = di.get(order)
#         direction = game_map[i][j]
#         next_i, next_j = i+move[0], j+move[1]
#         if i == next_i and j == next_j:
#             # Shoot
#             shoot(i, j, direction)
#         else:
#             # Move
#             next_direction = move[2]
#             game_map[i][j] = next_direction
#             if (0 <= next_i < H and 0 <= next_j < W) and game_map[next_i][next_j] == '.':
#                 game_map[i][j], game_map[next_i][next_j] = game_map[next_i][next_j], game_map[i][j]
#                 i, j = next_i, next_j
 
#     print('#{} '.format(tc), end='')
#     for ans in range(H):
#         print(''.join(game_map[ans][:]))