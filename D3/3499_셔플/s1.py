import sys
sys.stdin = open('sample_input.txt')

for tc in range(1, int(input()) + 1):
    N = int(input())
    card = list(input().split())
    ans = [0] * N
    if N % 2 == 0:
        for i in range(N // 2):
            ans[i * 2] = card[i]

        k = N // 2
        j = 1
        while j < N:
            ans[j] = card[k]
            j += 2
            k += 1
    else:
        for i in range(N // 2 + 1):
            ans[i * 2] = card[i]

        k = N // 2 + 1
        j = 1
        while j < N:
            ans[j] = card[k]
            j += 2
            k += 1


    print('#{} {}'.format(tc, ' '.join(ans)))







