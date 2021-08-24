T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 이동거리와 속도를 담을 변수 초기화   
    move = 0
    velocity = 0
    for _ in range(N):
        Command = list(map(int, input().split()))
        # 1이면 가속, 2이면 감속
        if Command[0] == 1:
            # 1이기 때문에 속도에 해당 값 추가
            veolocity += Command[1]        
        elif Command[0] == 2:
            # 2라서 감속해야하는데 원래 속도가 크면
            # 차이 만큼 감속
            if veolocity > Command[1]:
                veolocity -= Command[1]
            # 감속할 속도가 더 크면 속도는 0
            else:
                veolocity = 0
        # 속도만큼 이동하기, 0이면 현재 속도 유지이므로
        # 이전 속도만큼 이동
        move += veolocity

    print('#{} {}'.format(tc, move))

