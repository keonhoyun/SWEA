T = int(input())


def f(x, a):
    global ans
    if sum(x) == hlf:
        temp = [0, 0]
        k = [-1, 1]
        for i in range(n):
            temp[0] += k[x[i]] * arr[i][0]
            temp[1] += k[x[i]] * arr[i][1]
        ans = min(ans, temp[0] * temp[0] + temp[1] * temp[1])
        return
    elif a == n:
        return
    else:
        x[a] = 1
        f(x, a + 1)
        x[a] = 0
        f(x, a + 1)


for test_case in range(1, T + 1):
    n = int(input())
    hlf = int(n / 2)
    arr = [list(map(int, input().split())) for i in range(n)]
    ans = 99999999999999999
    ind = [0] * n
    f(ind, 0)
    print('#' + str(test_case), ans)