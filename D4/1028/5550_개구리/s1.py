def check(str):
    global flog
    for i in cry:
        if i == 'c':
            flog[i] += 1
        elif i == 'r':
            if flog['c'] > flog['r']:
                flog[i] += 1
            else:
                return -1
        elif i == 'o':
            if flog['c'] > flog['o'] and flog['r'] > flog['o']:
                flog[i] += 1
            else:
                return -1
        elif i == 'a':
            if flog['c'] > flog['a'] and flog['r'] > flog['a'] and flog['o'] > flog['a']:
                flog[i] += 1
            else:
                return -1
        elif i == 'k':
            if flog['c'] > flog['k'] and flog['r'] > flog['k'] and flog['o'] > flog['k'] and flog['a'] > flog['k']:
                flog[i] += 1
            else:
                return -1

    return 1






for tc in range(1, int(input()) + 1):
    flog = {'c': 0,
            'r': 0,
            'o': 0,
            'a': 0,
            'k': 0
            }

    cry = input()
    tmp = check(cry)
    ans = -1
    cnt = cry.count('croak')
    if tmp == 1:
        if flog['c'] >= flog['r'] >= flog['o'] >= flog['a'] >= flog['k']:
            if cnt == flog['k']:
                ans = 1
            else:
                ans = flog['c']
    print('#{} {}'.format(tc, ans))



