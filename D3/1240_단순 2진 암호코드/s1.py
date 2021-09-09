import sys
sys.stdin = open('input.txt')

ans = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9,
}

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [str(input()) for _ in range(N)]
    matrix = set(matrix)
    arr = list(matrix)
    start = -1
    result = []
    for i in range(1, len(arr)):
        for j in range(M - 1, -1, -1):            
            if arr[i][j] == '1':
                start = j
                break
        for k in range(start, -1, -7):
            code = ''
            for a in range(k, k-7, -1):
                code = arr[i][a] + code
            for key, value in ans.items():
                if key == code:
                    result.insert(0,value)
    sum_odd = 0
    sum_even = 0

    for i in range(0, len(result), 2):
        sum_odd += result[i]

    for i in range(1, len(result), 2):
        sum_even += result[i]

    total = (sum_odd * 3) + sum_even

    if total % 10:
        print('#{} 0'.format(tc))

    else:
        print('#{} {}'.format(tc, sum_even + sum_odd))

