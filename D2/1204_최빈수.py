T = int(input())
for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    # 갯수를 셀 리스트 생성
    cnt = [0] * 101
    
    # 배열을 돌며 cnt리스트의 해당 인덱스에 갯수 채워넣기
    for i in arr:
        cnt[i] = arr.count(i)

    # cnt의 마지막 값을 최빈수로 가정
    maxV = cnt[100]

    # 배열을 거꾸로 돌며(= 같으면 큰 수를 출력해야 하므로) 최빈수 교체하기
    for i in range(100, 0, -1):
        if maxV < cnt[i]:
            maxV = cnt[i]
            result = i

    print('#{} {}'.format(tc, result))
    
    

