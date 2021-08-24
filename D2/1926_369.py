N = int(input())
for i in range(1, N + 1): 
    # 3, 6, 9가 들어가면 몇 개 나오는지 갯수 세기   
    if '3' in str(i) or '6' in str(i) or '9' in str(i):
        a = str(i).count('3')
        b = str(i).count('6')
        c = str(i).count('9')
        cnt = a + b + c
        print('-'*cnt, end = ' ' )
    # 아니면 그냥 출력
    else:
        print(i, end = ' ')

    
    



            




        
        

                
        



            
