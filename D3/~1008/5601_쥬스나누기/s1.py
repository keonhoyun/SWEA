T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    ans = []
    for _ in range(N):
        a = '1/' + str(N)
        ans.append(a)
    print(f'# {tc}', end=" ")
    print(''.join(ans))
