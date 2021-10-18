import sys
sys.stdin = open('sample_input.txt')

keypad = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
          ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]


for tc in range(1, int(input()) + 1):
    S, N = input().split()
    N = int(N)
    words = list(input().split())


    ans = 0
    for word in words:
        cnt = 1
        j = 0
        if len(word) == len(S):
            while j < len(S):
                if word[j] in keypad[int(S[j])]:
                    cnt += 1
                    j += 1
                j += 1
            if cnt == len(S):
                ans += 1


    print('#{} {}'.format(tc, ans))






