import sys
sys.stdin = open('input.txt')

T = 10
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for j in range(N):
        temp_stack = []             
        for i in range(N):
            if arr[i][j] == 1:
                temp_stack.append(1)
            if arr[i][j] == 2 and temp_stack:
                temp_stack.clear()
                cnt += 1
 
    print("#{} {}".format(t, cnt))