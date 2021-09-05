T = int(input())

for tc in range(1, T + 1):
    original = list(map(str, input()))
    N = len(original)
    # 갯수를 셀 변수 초기화    
    cnt = 0 
   
    # 원래 값이 1로 시작하면 cnt를 1로 변경
    if int(original[0]) == 1:
        cnt = 1
    # 1번 인덱스부터 시작
    i = 1                 
    while i < N:
        # 만약 인덱스 값이 0이면
        if int(original[i]) == 0:
            # 앞의 값이 0이면 다음 인덱스로
            if int(original[i - 1]) == 0:
                i += 1            
            # 앞의 값이 1이면 cnt를 1추가하고 다음 인덱스로(1로 바뀌어 있기 때문)
            elif int(original[i - 1]) == 1:
                cnt += 1
                i += 1                        
        # 만약 인덱스 값이 1이면
        elif int(original[i]) == 1:
            # 앞 인덱스 값이 1이면 다음 인덱스로
            if int(original[i - 1]) == 1:
                i += 1
            # 앞 인덱스 값이 0이면 cnt 1추가하고 다음 인덱스로(0으로 바뀌어 있기 때문)
            elif int(original[i - 1]) == 0:
                cnt +=1
                i += 1                 

    print('#{} {}'.format(tc, cnt))
    


            
        
        
        
        

