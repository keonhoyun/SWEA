import sys
sys.stdin = open('input.txt')

arr = [0] * (10002 ** 2)
n = 1
k = 2

while n <= 10001 ** 2:
    for i in range(1, k):
        x = 0
        y = k
        arr[n] = (x + i, y - i)
        n += 1
    k += 1



for tc in range(1, int(input()) + 1):
    p, q = map(int, input().split())

    temp_a = arr[p]
    temp_b = arr[q]
    temp_ans = (temp_a[0] + temp_b[0], temp_b[1] + temp_b[1])
    result = arr.index((temp_ans[0], temp_ans[1]))
    print('#{} {}'.format(tc, result))
