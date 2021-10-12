# 시작일자 요일로 만든 딕셔너리
calendar = {
    '1': 4,
    '2': 0,
    '3': 1,
    '4': 4,
    '5': 6,
    '6': 2,
    '7': 4,
    '8': 0,
    '9': 3,
    '10': 5,
    '11': 1,
    '12': 3,
}


for tc in range(1, int(input()) + 1):
    M, D = map(int, input().split())
    # 시작 월의 시작 요일 받아오기
    start = calendar[str(M)]
    # 몇일 차이인지 계산
    day = (D - 1) % 7
    # 요일 계산
    ans = (start + day) % 7

    print('#{} {}'.format(tc, ans))

