for tc in range(1, int(input()) + 1):
    N = int(input())
    ans = []
    for _ in range(N):
        p, x = map(float, input().split())
        ans.append(p * x)
    result = sum(ans)

    print('#{} {:.6f}'.format(tc, result))