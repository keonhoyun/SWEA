for tc in range(1, int(input()) + 1):
    # 빈 딕셔너리 생성
    tmp = {}
    words = input()
    # 리스트를 돌며 딕셔너리에 있는 단어인지 확인
    for word in words:
        if word not in tmp:
            tmp[word] = 1
        # 있으면 1씩 추가하기
        else:
            tmp[word] += 1
    ans = 0
    # 필렌드롬의 최대갯수는 길이 * (길이 + 1) // 2 만큼 생성된다.
    # 예를 들어 aaaa인 경우 a, a, a, a, aa, aa, aa, aaa, aaa, aaaa로 총 10개(4 * 5 // 2)
    # 그래서 최대로 만들 수 있는 갯수를 더하면 된다.
    # 예를 들어 aabb 이면 a, a, b, b, aa, bb로 총 6개 (2 * 3 // 2) + (2 * 3 // 2)
    for k in tmp.keys():
        ans += (tmp[k]*(tmp[k]+1))//2

    print('#{} {}'.format(tc, ans))