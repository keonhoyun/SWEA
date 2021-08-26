
# 성적등급을 가지는 리스트 선언, 나중에 오름차순으로 정렬함으로 낮은 등급부터 작성
grade = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']

T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    # 학생들의 성적을 담을 빈 리스트 선언    
    rank = []
    for _ in range(N):
        # 중간, 기말, 과제 성적 받아오기      
        Mid_test, Fin_test, report = map(int, input().split())
        record = Mid_test * 0.35 + Fin_test * 0.45 + report * 0.2
        # 성적리스트에 집어 넣기
        rank.append(record)
    # 원하는 학생의 성적 받아오기
    chk_num = rank[K -1]

    # 오름차순 정렬
    sort_rank = sorted(rank)
    
    # 해당 학생이 몇번째인지 받아오기
    idx = (sort_rank.index(chk_num) + 1)

    # 10등분을 해야함으로 총 학생수를 10으로 나누기
    grade_idx = N // 10
   

    # 만약 홀수번째이면 인덱스는 몫
    if idx % grade_idx:
        result = idx // grade_idx

    # 만약 짝수번째이면 인덱스는 몫 -1 
    else:
        result = idx // grade_idx -1


    print('#{} {}'.format(tc, grade[result]))
    
    






    
    

    

    
    
        
