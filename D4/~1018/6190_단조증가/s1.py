import sys
sys.stdin = open('s_input.txt')

def danjo(ans):
    for i in range(len(ans) - 1):
        if ans[i] > ans[i + 1]:
            return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    maxV = 0
    for i in range(N-1):
        for j in range(i + 1, N):
            ans = str(arr[i] * arr[j])
            if danjo(ans):
                if maxV < int(ans):
                    maxV = int(ans)
        if maxV == 0:
            maxV = -1


    print('#{} {}'.format(tc, maxV))

# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     numbers = []
#     maxV = 0
#     for i in range(N-1):
#         for j in range(i + 1, N):
#             ans = arr[i] * arr[j]
#             if ans % 10:
#                 numbers.append(ans)
#
#
#     for number in numbers:
#         a = str(number)
#         k = 0
#         if len(a) > 1:
#             while k < (len(a) - 1):
#                 if int(a[k]) > int(a[k + 1]):
#                     numbers.remove(number)
#                     k += 1
#                 else:
#                     k += 1
#     result = max(numbers)
#
#     if not numbers:
#         result = -1
#
#     print('#{} {}'.format(tc, result))





































