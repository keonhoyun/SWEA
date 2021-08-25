# 날짜를 판별할 딕셔너리 생성
calendar = {
    '01': 31,
    '02': 28,
    '03': 31,
    '04': 30,
    '05': 31,
    '06': 30,
    '07': 31,
    '08': 31,
    '09': 30,
    '10': 31,
    '11': 30,
    '12': 31,
}

T = int(input())
for tc in range(1, T + 1):
    date = str(input())
# 월이 1~12를 벗어나는 경우
    if int(date[4:6]) < 1 or  int(date[4:6]) > 12:
        result = -1
# 날짜 형식이 정확한 경우
    elif calendar.get(date[4:6]) >= int(date[6:8]):
        result = date[0:4] + '/'+ date[4:6] + '/' + date[6:8]
# 그 이외 경우
    else:
        result = -1
    print('#{} {}'.format(tc, result))
        
