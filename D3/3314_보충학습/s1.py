T = int(input())
for tc in range(1, T + 1):
    # 학생들 성적 받아오기
    scores = list(map(int, input().split()))
    # 원래 성적의 합 받아오기
    origin_sum = sum(scores)
    # 보충학습을 하면 40점으로 됨으로
    # 40점 미만인 점수와 40점의 차이 만큼 더해주기
    for score in scores:
        if score < 40:
            origin_sum += (40 - score)
    # 5명이므로 5로 나눠주기
    print(f'#{tc} {int(origin_sum / 5)}')