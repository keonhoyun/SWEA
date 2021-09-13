           
T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    members = list(map(int, input().split()))
    long = len(members)
    tops = []

    # 부분집합 구하기
    for i in range(1 << long):
        ans = []
        for j in range(long):
            if i & (1 << j):
                ans.append(members[j])
        # 런타임 에러를 제거하기 위해 
        # 부분집합의 합을 바로 리스트에 넣기
        tops.append(sum(ans)) 

    # 최소값 초기화
    minV = 100
    for top in tops: 

        # 선반보다 낮으면 패스
        if top < B:
            continue
        # 선반보다 높으면 최소값과 비교
        else:
            result = (top - B)
            if result < minV:
                minV = result

    print('#{} {}'.format(tc, minV))


# 런타임 에러 발생
# import itertools

# T = int(input())
# for tc in range(1, T + 1):
#     N, B = map(int, input().split())
#     members = list(map(int, input().split()))
#     tops = []
#     for i in range(1, len(members) + 1):
#         part = itertools.permutations(members, i)
#         tops.extend(part)  
    
#     minV = 100
#     for top in tops:
#         ans = sum(top)

#         if ans < B:
#             continue

#         else:
#             result = (ans - B)
#             if result < minV:
#                 minV = result

#     print('#{} {}'.format(tc, minV))
            
                
