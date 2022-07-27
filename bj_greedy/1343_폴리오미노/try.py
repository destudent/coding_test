X=input()
change=-1
tmp=''
arr_X=[0]*50
arr_dot=[0]*50
for i in range(len(X)):
    if tmp != X[i]:
        change+=1
        tmp=X[i]
    if X[i]=='X':
        arr_X[change]+=1
    if X[i]=='.':
        arr_dot[change]+=1

result=[]
err=0
for i in range(len(arr_X)):
    if arr_X[i]>0:
        if arr_X[i]%2==0:
            AAAA=arr_X[i]//4
            if AAAA !=0:
                result.append(AAAA*'AAAA')
            BB=arr_X[i]%4
            if BB !=0:
                result.append(BB*'B')
        else:
            print('-1')
            err+=1
            break
    if arr_dot[i]>0:
        dot=arr_dot[i]
        result.append(dot*'.')
if err==0:
    for i in range(len(result)):
        print(result[i],end='')
