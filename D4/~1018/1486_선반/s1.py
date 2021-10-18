           
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    members = list(map(int, input().split()))    
    tops = []

    minV = 100
    # 부분집합 구하기
    for i in range(1 << N):
        ans = 0
        for j in range(N):
            if i & (1 << j):
                ans += members[j]
        
        if B <= ans <= minV:
            minV = ans
    result = minV - B   

    print('#{} {}'.format(tc, result))


# 런타임 에러 발생
# import itertools

# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     members = list(map(int, input().split()))
#     tops = []
#     minV = 99999999999999999
#     for i in range(1, len(members) + 1):
#         part = sum(itertools.permutations(members, i))
#         if B <= part <= minV:
#             minV = part
#     result = part - B

#     print('#{} {}'.format(tc, result))

    
   
   
            
                
