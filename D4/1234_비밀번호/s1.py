import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N, numbers = map(str, input().split())
    stack = []
    for number in numbers:
        if stack: # stack이 비어있지 않다면
            if stack[-1] == number: # 반복된 문자라면
                stack.pop()
            else: # 반복된 문자가 아니라면 stack에 추가
                stack.append(number)

        else: # 스텍이 비어있으면 비교없이 바로 추가
            stack.append(number)

    print('#{} {}'.format(tc, ''.join(stack)))










