
for tc in range(1, int(input()) + 1):
    A, B, C = map(int, input().split())
    A_cnt = 0
    B_cnt = 0
    if A < B:
        A_cnt = C // A
        change = (C % A)
        if B < change:
            B_cnt = change // B

    elif B < A:
        B_cnt = C // B
        change = C % B
        if A < change:
            A_cnt = change // A

    else:
        A_cnt = C // A


    result = A_cnt + B_cnt

    print('#{} {}'.format(tc, result))

