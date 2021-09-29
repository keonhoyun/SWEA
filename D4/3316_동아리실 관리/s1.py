for tc in range(1, int(input()) + 1):
    managers = input()

    case = 8 ** (len(managers) - 1) * 4
    impossible = 3 + (len(managers) - 2) * 7

    if managers[0] == 'A':
        case = 8 ** (len(managers))
        impossible = 6 + (len(managers) - 2) * 7
    result = case - impossible

    print('#{} {}'.format(tc, result % 1000000007))

