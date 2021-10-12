for tc in range(1, int(input()) + 1):
    S = list(input())

    if S.count(S[0]) == 2:
        if S[0] != S[1]:
            if S.count(S[1]) == 2:
                ans = 'Yes'
        else:
            if S.count(S[2]) == 2:
                ans = 'Yes'
    else:
        ans = 'No'

    print('#{} {}'.format(tc, ans))

