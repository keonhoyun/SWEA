def double(N, M):
    if M == 1:
        return N
    else:
        return N * double(N, M-1)    


for _ in range(10):
    tc = int(input())
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, double(N, M)))

