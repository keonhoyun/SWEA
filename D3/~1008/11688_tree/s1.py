
T = int(input())
for tc in range(1, T+1):
    # 루트 받아오기
    roots = input()
    # L값과 R값 1로 초기화
    L = 1
    R = 1
    # 문자열을 돌면서 L과 R확인
    for root in roots:
        if root == 'L':
            L = L
            R = L + R
        else:
            L = L + R
            R = R

    print('#{} {} {}'.format(tc, L, R))