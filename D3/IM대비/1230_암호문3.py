for tc in range(1, 11):
    N = int(input())
    password = list(map(int, input().split()))

    M = int(input())
    command = list(map(str, input().split()))
    i = 0
    while i < M:    
        if command[i] == 'I':
            x = int(command[i + 1])
            y = int(command[i + 2])
            s = list(command[i + 3: i + 3 + y])
            for j in range(y):
                password.insert(x+j, s[j])
            i += (x+y)           
        
        elif command[i] == 'D':
            x = int(command[i + 1])
            y = int(command[i + 2])
            for _ in range(y):
                password.pop(x-1)
            i += (x+y)            

        elif command[i] == 'A':            
            y = int(command[i + 1])
            s = list(command[i + 2: i + 2 + y])
            for j in range(y):
                password.append(s[j])            
            i += (y+s)

        else:
            i += 1

    result = []
    for j in range(10):
        result.append(password[j])


    print('#{}'.format(tc), end = ' ')
    print(' '.join(map(str, result)))

            
    
    




    