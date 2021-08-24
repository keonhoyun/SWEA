T = int(input())
for tc in range(1, T + 1):    
    text = str(input())
    # 반복되는 문자가 있는지 확인하기
    # 문자열 길이의 중간을 기준으로 좌측만 검사
    for M in range(len(text)//2):
        # 반복문을 돌며 한글자씩 늘리며 반복되는지 검사
        # 만약 반복되면 해당 길이인 M을 저장
        if text[0: M+1] == text[M+1:(M+1)*2]:
            result = M
            break
    # 반복문의 길이를 활용 반복되는 단어 도출
    word = text[0:result+1]
    
    # 몇 번 반복된는지 갯수 세기 
    print('#{} {}'.format(tc, text.count(word)-1))