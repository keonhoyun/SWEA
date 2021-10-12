change = {
    'q': 'p',
    'p': 'q',
    'b': 'd',
    'd': 'b'
}


for tc in range(1, int(input()) + 1):
    text = list(input())
    ans = []
    for i in range(len(text) - 1, -1, -1):
        ans.append(change[text[i]])

    result = ''.join(ans)
    print('#{} {}'.format(tc, result))



