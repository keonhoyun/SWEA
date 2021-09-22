T = int(input(0))
for tc in range(1,T + 1):
    p, q = map(float, input().split())
    # 한 번 뒤집어서 꽂히는 경우
    # 뒤집어서 꽂을 확률에 제대로 꽂힐 확률
    s1 = (1-p)*q

    # 두 번 뒤집어서 꽂히는 경우
    # 원래 제대로 꽂을 확률에 안 꽂힐 확률 X 제대로 꽂을 확률
    s2 = p*(1-q)*q
    result = 'YES'
    if s1  < s2:
        result = 'NO'

    print("#{} {}".format(tc, result))