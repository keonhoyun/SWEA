import sys
sys.stdin = open('input_1244.txt')
#
T = int(input())
for tc in range(1, T + 1):
    bonus, N = map(int, input().split())
    bonus_lst = list(map(int, str(bonus)))
    maxV = bonus_lst[-1]
    for i in range(len(bonus_lst) - 1, -1, -1):
        if maxV < bonus_lst[i]:
            maxV = bonus_lst[i]
    Idx = bonus_lst.index(maxV)
    minIdx = bonus_lst.index(min(bonus_lst))

    if N == 1:
        if Idx != 0:
            bonus_lst[0], bonus_lst[Idx] = bonus_lst[Idx], bonus_lst[0]
        else:



    if N > 1:



T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
def dfs(c):
    global answer
    if c == 0:
        answer = max(answer, int("".join(nums)))
        return
     
    for i in range(length-1):
        for j in range(i+1, length):
            nums[i], nums[j] = nums[j], nums[i]
             
            if (int("".join(nums)), c) not in visited:
                visited[(int("".join(nums)), c)] = 1
                dfs(c-1)
                 
            nums[i], nums[j] = nums[j], nums[i]
             
 
 
 
 
for test_case in range(1, T + 1):
    nums, c = input().split()
    c = int(c)
    nums = list(nums)
    length = len(nums)
    visited = {}
    answer = -9999999
    dfs(c)
    print(f"#{test_case} {answer}")







