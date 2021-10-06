import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 0:
                start = [i, j]
                cnt += 1
                row = 1
                column = 1
            while True:
                ni = i + 1
                if arr[ni][j] != 0:
                    row += 1
                else:
                    break

            while True:
                nj = j + 1
                if arr[i][j] != 0:
                    column += 1
                else:
                    break

            for k in range(row):
                for h in range(column):
                    arr[k][h] = 0
    print(cnt)

