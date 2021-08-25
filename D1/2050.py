alpha = input()
# 아스키코드를 활용하여 숫자로 변환
for i in range(len(alpha)):
    print(ord(alpha[i])-64, end = ' ')