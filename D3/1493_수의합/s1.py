def new_num():  # 1 ~ 10000 까지의 정수가 주어지니까 해당 정수들이 가질 수 있는 좌표들을 미리 구해놓자
    result = [0] * 50001  # 최종은 둘을 더하는 좌표가 되니까 50000까지 구해보자
    idx = 1
    i = 2
    while True:
        for j in range(1, i):  # 대각선은 합이 i 인 좌표들이 모여있게 된다
            result[idx] = (j, i - j)
            idx += 1
            if idx == 50001:
                return result
        i += 1


def new_calc(n1, n2):
    new_x = numbers[n1][0] + numbers[n2][0]
    new_y = numbers[n1][1] + numbers[n2][1]
    return numbers.index((new_x, new_y))


T = int(input())
numbers = new_num()
for test_case in range(1, T + 1):
    n1, n2 = map(int, input().split())
    print('#{} {}'.format(test_case, new_calc(n1, n2)))