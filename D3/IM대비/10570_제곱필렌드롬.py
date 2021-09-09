for tc in range(1, int(input()) + 1):
    # A, B 구해오기
    A, B = map(int, input().split())
    cnt = 0
    for i in range(A, B + 1):
        # 제곱근 구하기
        C = i ** (1 / 2)
        # 제곱근이 정수변환했을 때 같다면
        if C == int(C):
            # 회문인지 검사
            i = str(i)
            C = str(int(C))
            # 회문이면 cnt + 1
            if i == i[::-1] and C == C[::-1]:
                cnt += 1

    print(f'#{tc} {cnt}')


        

        

    

