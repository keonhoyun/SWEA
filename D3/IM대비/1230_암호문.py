# import sys
# sys.stdin = open('input.txt')

# for tc in range(1, 11):
#     N = int(input())
#     password = list(map(int, input().split()))

#     M = int(input())
#     command = list(map(str, input().split()))

#     for i in range(M):
#         if command[i] == 'I':
#             for j in range(1, int(command[i + 2]) + 1):
#                 password.insert(int(command[i + 1]), int(command[i + 2 + j]))
        
#         elif command[i] == 'D':
#             for _ in range(int(command[i + 2])):
#                 password.pop(int(command[i+1])+1)

#         elif command[i] == 'A':
#             for j in range(1, int(command[i + 1]) + 1):
#                 password.append(int(command[i + 1 + j]))

#         elif command[i] != 'I' and command[i] != 'D' and command[i] != 'A':
#             i += 1

#     print('#{}'.format(tc), end = ' ')
#     print(' '.join(map(str, password)))

            
    
    




    