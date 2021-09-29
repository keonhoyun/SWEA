for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    # 선택된 종목의 횟수 구할 빈 리스트
    ans = [0] * len(Ai)

    for B in Bi:
        for i in range(len(Ai)):
            # 조건에 맞는 종목 찾기
            if Ai[i] <= B:
                ans[i] = ans[i] + 1

    # 최대값 초기화
    maxV = ans[0]
    for i in range(len(ans)):
        # 최대값이 나타나면 바구기
        if maxV < ans[i]:
            maxV = ans[i]
            # 인덱스 받아오기
            idx = i

    print('#{} {}'.format(tc, idx))