T = int(input())
for test_case in range(1, T + 1):
    n, pd, pg = map(int, input().split())
    result = ""
    if pg == 100 and pd != 100:
        result = "Broken"
    elif pg == 0 and pd != 0:
        result = "Broken"
    else:
        result = "Broken"
        if n >= 100:
            result = "Possible"
        else:
            for j in range(1, n + 1):
                if j * pd % 100 == 0:
                    result = "Possible"
                    break

    print("#%d %s" % (test_case, result))