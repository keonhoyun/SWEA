for tc in range(1, int(input()) + 1):
    text = list(input())
    H = int(input())
    location = list(map(int, input().split()))
    for i in range(len(location)):
        if location[i] != 0:
            text[location[i] - 1] = text[location[i] - 1] + '-'
        else:
            text[0] = '-' + text[0]


    print('#{} {}'.format(tc, ''.join(text)))
