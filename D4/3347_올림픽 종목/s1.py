
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    Ai = list(map(int, input().split()))
    Bi = list(map(int, input().split()))

    # 선택된 종목의 횟수 구할 빈 리스트
    ans = [0] * len(Ai)

    for B in Bi:
        i = 0
        while i < len(Ai):
            if Ai[i] <= B:
                ans[i] = ans[i] + 1
                i += 1
            else:
                i += 1

    maxV = ans[0]
    for j in range(len(ans)):
        if maxV < ans[j]:
            maxV = ans[j]
            idx = j

    print('#{} {}'.format(tc, idx))


