a_hand, b_hand = map(int, input().split())
# a가 가위일때 
if a_hand == 1:
    if b_hand == 2:
        print('B')
    else:
        print('A')
# a가 바위일때         
if a_hand == 2:
    if b_hand == 3:
        print('B')
    else:
        print('A')
# a가 보일때         
if a_hand == 3:
    if b_hand == 1:
        print('B')
    else:
        print('A')
