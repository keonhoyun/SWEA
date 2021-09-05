for tc in range(1, 11):
    N = int(input())
    arr = [input() for _ in range(8)]    

    cnt = 0
    # 회문인지 판별하는 반목문 생성
    for i in range(8):
        for j in range(8 - N + 1):
            # 회문이 있다고 가정
            ans = 1
            # 중앙값을 기준으로 왼쪽만 판별
            for k in range(N//2):
                # 만약 회문이 아니면 ans 0으로 초기화
                if arr[i][j + k] != arr[i][j + N -1 -k]:
                    ans *= 0
                # 만약 같다면 계속 검사하기
                elif arr[i][j + k] == arr[i][j + N -1 -k]:
                    ans *= 1
            # 반목문을 돌렸을 때 1이면 회문이므로
            if ans == 1:
                cnt += 1                
            

    for i in range(8):
        for j in range(8 - N + 1):
            ans = 1
            for k in range(N//2):
                if arr[j + k][i] != arr[j + N -1 -k][i]:
                    ans *= 0
                elif arr[j + k][i] == arr[j + N -1 -k][i]:
                    ans *= 1
            if ans == 1:
                cnt += 1
    
    print('#{} {}'.format(tc, cnt))
    


            

    
