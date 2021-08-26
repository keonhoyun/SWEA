import sys

sys.stdin = open('input.txt')
# 스도쿠 검사 함수 생성
def sdoque(arr):
    # 스도쿠는 각각 0번, 3번, 6번 인덱스를 기준으로 3X3행렬 안을 탐색
    i_lst = [0, 3, 6]
    h_lst = [0, 3, 6]
    for h in h_lst:
        for i in i_lst:
            chk_set = set()
            # 3x3 행렬을 탐색하며 세트에 집어넣기
            for j in range(3):
                for k in range(3):
                    chk_set.add(arr[i + j][i + k])
            # 세트는 중복이 제거됨으로 스도쿠라면 길이가 9일 것
            # 스도쿠가 아니면 0을 반환
            if len(chk_set) != 9:
                return 0
    # 행 탐색
    for i in range(9):
        chk_set2 = set()
        for j in range(9):
            # 1행부터 세트에 집어넣기
            chk_set2.add(arr[i][j])
        # 세트는 중복이 제거됨으로 스도쿠라면 길이가 9일 것
        # 스도쿠가 아니면 0을 반환
        if len(chk_set2) != 9:
            return 0

    for i in range(9):
        chk_set3 = set()
        # 1열부터 세트에 집언허기
        for j in range(9):
            chk_set3.add(arr[j][i])
        # 세트는 중복이 제거됨으로 스도쿠라면 길이가 9일 것
        # 스도쿠가 아니면 0을 반환
        if len(chk_set3) != 9:
            return 0
    return 1

T = int(input())
for tc in range(1, T + 1):
    # 스도쿠 배열 받아오기
    arr = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(tc, sdoque(arr)))
























