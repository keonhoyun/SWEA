T = int(input())
for tc in range(1, T + 1):
    arr = list(map(int, input().split()))
    ans = 0
# 배열을 돌며 값 더하기
    for i in arr:
        ans += i
# 반올림으로 문제가 원하는 정수 형태로 나타내기
    print('#{} {}'.format(tc, (round(ans/len(arr)))))