# 두 자리 수의 곱 세트 자료형으로 만들기
gugudan = set()
for i in range(1, 10):
    for j in range(1, 10):
        gugudan.add(i * j)


for tc in range(1, int(input()) + 1):
    number = int(input())
    # 결과값 No로 초기화
    ans = 'No'
    if number in gugudan:
        # 만약 세트 자료형에 있다면 Yes 반환
        ans = 'Yes'

    print('#{} {}'.format(tc, ans))