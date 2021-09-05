T = int(input())
# 모음인지 검사할 리스트 생성
aeiou = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, T + 1):
    # 대문자가 끼어있을 수 있으므로 소문자로 변환
    word = input().lower()
    # 자음만 담을 빈 문자열 생성
    result = ''
    # 자음인지 검사하기
    for i in word:
        if not i in aeiou:
            result += i
    print('#{} {}'.format(tc, result))

            



