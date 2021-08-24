T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))

    # 마지막 값을 팔 가격으로 가정
    sell = arr[-1]
    # 이윤 0 으로 초기화
    gain = 0
    # 뒤부터 배열 돌기
    for i in range(N-1, -1, -1):
        # 팔 가격이 계속 높다면 그 가격에 팔기
        if sell > arr[i]:
            gain += (sell - arr[i])
        # 팔 가격보다 살 가격이 높다면
        # 팔 가격을 바꾸기
        elif sell < arr[i]:
            sell = arr[i]
    print('#{} {}'.format(tc, gain))
