T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # 모두 뿔 한 개씩 가지고 있다고 가정하면
    # N - M 만큼 트윈혼 마리수가 됨
    twinhon = N - M

    # 전체 마리에서 트윈혼 개수 빼기
    unicon = M - (N - M)
    
    print('#{} {} {}'.format(tc, unicon, twinhon))