for tc in range(1, int(input()) + 1):
    texts = list(input())
    stack = []
    tmp = set()

    for text in texts:
        if texts.count(text) == 1:
            stack.append(text)
        elif texts.count(text) % 2:
            tmp.add(text)
        else:
            continue

    tmp = list(tmp)

    stack = stack + tmp


    result = 'Good'

    if stack:
        result = ''.join(sorted(stack))
    print('#{} {}'.format(tc, result))












