T = int(input())
for tc in range(1, T + 1):
# map으로 각각 a,b 구하고 몫과 나머지 구하기
    a, b = map(int, input().split())
    div = a // b
    rest = a % b
    print('#{} {} {}'.format(tc, div, rest))