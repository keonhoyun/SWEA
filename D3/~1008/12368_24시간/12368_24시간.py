T = int(input())
for tc in range(1, T + 1):
    # A와 B받아오기
    A, B = map(int, input().split())
    # 먼저 더한 값을 기본값으로 설정
    result = A + B
    # 만약 정확히 24면 0
    if result == 24:
        result = 0
    # 24보다 크면 24를 빼서 반환
    elif result > 24:
        result -= 24
    print('#{} {}'.format(tc, result))
