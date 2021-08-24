
date_dict = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}

T = int(input())
for tc in range(1, T + 1):
    # 앞 날짜의 월과 일, 뒷 날짜의 월과 일 받아오기
    month1, day1, month2, day2 = map(int, input().split())
    # 월이 같은 경우 일의 차이에서 + 1 만큼을 저장    
    if month1 == month2:
        date = day2 - day1 + 1
    else:
        # 월이 다른 경우 날짜 값을 0으로 초기화(=반복문 돌리기 위함)
        date = 0
        # 반복문을 돌며 딕셔너리의 value값 더하기(앞 날짜의 바로 다음 월부터)
        for i in range(month1 + 1, month2):
            date += date_dict[str(i)]
        # 반복문을 돌린 결과의 뒷 날짜의 일수와 앞 날짜의 마지막일에서 앞 날짜의 일을 뺀 값을 저장
        date = date + day2 + date_dict[str(month1)] - day1 + 1

    print('#{} {}'.format(tc, date))
