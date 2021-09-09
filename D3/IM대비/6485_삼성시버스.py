# 버스 도착 횟수 세는 함수 생성
def bus_count(bus_stop):
    cnt = 0
    # 정류장이 버스 루트 안에 있으면 cnt + 1
    for i in range(N):
        if bus_rout[i][0] <= bus_stop <= bus_rout[i][0]:
            cnt += 1
    return cnt

for tc in range(1, int(input()) + 1):
    N = int(input())
    bus_rout = []
    for i in range(N):
        A, B = map(int, input().split())
        # 버스루트를 튜플로 받아오기
        bus_rout.append((A,B))

    P = int(input())
    ans = []
    for i in range(P):
        C = int(input())
        ans.append(bus_count(C))
    print('#{}'.format(tc), end = ' ')
    print(' '.join(map(str, ans)))


