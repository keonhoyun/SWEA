import sys
sys.stdin = open('sample_input.txt')

# N값 받아오기
N = int(input())
# N값 만큼 반목하여 전환할 문자 받아오기
for _ in range(N):
    words = str(input())
    # 기본 배열을 모두 "."인 이차원 배열 만들기
    # 배열의 길이는 4 * 문자의 길이 + 1
    # ex) D면 5, APPLE이면 21    
    arr = [['.'] * (4 * len(words) + 1) for _ in range(5)]
    
    for i in range(1, 6):
        # 2차원 배열 첫번째행과 마지막행
        if i == 1 or i == 5:
            for j in range(2, 4 * len(words) + 1, 4):
                arr[i - 1][j] = '#'
        # 2차원 배열 2번째 행과 4번째 행
        if i % 2 == 0:
            for j in range(1, 4 * len(words) + 1, 2):
                arr[i - 1][j] = '#'
        # 3번째 행
        if i == 3:
            for j in range(0, 4 * len(words) + 1, 4):
                arr[i - 1][j] = '#'
            # 3번째 행에서 2번 인덱스부터 4단위로 단어로 교환
            k = 0
            for j in range(2, 4 * len(words) + 1, 4):
                arr[i - 1][j] = words[k]
                k += 1
    # 출력하기
    for ans in arr:
        print(''.join(ans))
   
                

        



    




