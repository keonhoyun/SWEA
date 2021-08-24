

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    money = [0] * 8
    # 돈이 10원 이상 남아 있으면 계속 반복문 돌리기
    while N >= 10:
        # 5만원 보다 크면 5만원 먼저 거슬러주기
        if N >= 50000:
            money[0] = N // 50000
            N -= (50000 * money[0])

        # 다음 만원 거슬러 주기
        elif N >= 10000:
            money[1] = N // 10000
            N -= (10000 * money[1])
        
        elif N >= 5000:
            money[2] = N // 5000
            N -= (5000 * money[2])

        elif N >= 1000:
            money[3] = N // 1000
            N -= (1000 * money[3])

        elif N >= 500:
            money[4] = N // 500
            N -= (500 * money[4])

        elif N >= 100:
            money[5] = N // 100
            N -= (100 * money[5])

        elif N >= 50:
            money[6] = N // 50
            N -= (50 * money[6])
        # 마지막 10원까지 거슬러주면 거스름돈 끝
        elif N >= 10:
            money[7] = N // 10
            N -= (10 * money[7])
            
    # 빈칸을 포함해서 숫자 출력하기 위해 string으로 변환
    conveted_lst = [str(i) for i in money]
    ans = ' '.join(conveted_lst)

    print('#{}'.format(tc))
    print(ans)



        
    
