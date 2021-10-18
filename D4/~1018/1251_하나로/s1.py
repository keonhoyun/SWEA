T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    X_list = []
    Y_list = []
    for _ in range(N):
        X, Y = map(int, input().split())
        X_list.append(X)
        Y_list.append(Y)