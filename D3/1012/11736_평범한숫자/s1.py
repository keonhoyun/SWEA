for tc in range(1, int(input()) + 1):
    N = int(input())
    numbers = list(map(int, input().split()))
    cnt = 0
    for i in range(1, N - 1):
        if numbers[i] < numbers[i + 1] and numbers[i] > numbers[i - 1]:
            cnt += 1

        elif numbers[i] > numbers[i + 1] and numbers[i] < numbers[i - 1]:
            cnt += 1



    print('#{} {}'.format(tc, cnt))



