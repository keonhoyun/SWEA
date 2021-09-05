for _ in range(1, 11):
    tc = int(input())
    # 배열 받아오기
    arr = list(map(int, input().split()))
    # i = 1로 초기화
    i = 1
    while True:
        # i > 5면 1로 초기화
        if i > 5:
            i = 1
        # 첫번째 값 꺼내서 - i
        password = arr.pop(0) - i

        # 만약 꺼낸 값이 0이하면 0으로 설정
        # 반복문 종료
        if password <= 0:
            arr.append(0)
            break
        # 꺼낸 값 맨 뒤로 추가
        # i + 1
        arr.append(password)
        i += 1

    print('#{}'.format(tc), end = ' ')
    print(' '.join(map(str, arr)))