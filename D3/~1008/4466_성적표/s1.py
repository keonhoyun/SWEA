T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))
    # ans = sorted(scores, reverse=True)
    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if scores[j] < scores[j + 1]:
                scores[j], scores[j + 1] = scores[j + 1], scores[j]
    result = 0
    for i in range(K):
        result += scores[i]
    
    print('#{} {}'.format(tc, result))
    
    
 # 버블정렬





    
    

   
    
        

    

 
