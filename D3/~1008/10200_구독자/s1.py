T = int(input())
for tc in range(1, T + 1):
    N, A, B = map(int, input().split())
    maxV = min(A, B)
    if A + B > N:
        minV = (A + B) - N
    else:
        minV = 0
    



    print('#{} {} {}'.format(tc, maxV, minV))