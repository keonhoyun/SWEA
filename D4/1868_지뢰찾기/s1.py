di = [1, 1, 0, -1, -1, -1, 0, 1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

def is_mine(x, y):
    if (0 <= x < N) and (0 <= y < N) and mines[x][y] == '*':
        return True
    return False    

def is_zero(x, y):
    for direct in range(8):
        ni = x + di[direct]
        nj = y + dj[direct]
        if is_mine(ni, nj):
            return False
    return True

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    mines = [list(input()) for _ in range(N)]
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if mines[i][j] == '.' and is_zero(i, j):
                pass
   