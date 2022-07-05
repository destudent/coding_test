n = int(input()) # 좌석수 = 사람수
sit = input()
couple = 0 # LL연속 구분장치
cup = 0

if len(sit) > 1: #길이가 1 보다 길 때
    if sit[0] == 'S': # 0번째 배열이 S면 양옆 컵홀더 2개
        cup = 2
    if sit[0] == 'L': # 0번째 배열이 L이면 맨왼쪽 컵홀더 1개만 존재
        cup = 1
        couple+=1

for i in range(1,n):

    if sit[i-1]=='L' and sit[i]=='L' and couple ==1:
        cup +=1
        couple = 0

    elif sit[i] == 'L':
        couple+=1


    if sit[i] == 'S':
        cup +=1

    

if n > cup :
    print(cup)
else:
    print(n)
