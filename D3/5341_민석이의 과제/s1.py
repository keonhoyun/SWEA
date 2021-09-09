T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    people = list(range(1, N + 1))
    submit = list(map(int, input().split()))
    ans = []
    for person in people:
        if not person in submit:
            ans.append(str(person))

    
    print('#{}'.format(tc), end=' ')
    print(' '.join(ans))

    


