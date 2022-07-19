

lpv=[]
while 1:
    lpv.append(list(map(int,input().split())))
    if lpv[-1]==[0,0,0]:
        lpv.pop()
        break


for i in range(len(lpv)):
    vacation=0
    vacation += lpv[i][0]*(lpv[i][2]//lpv[i][1])
    if lpv[i][0]>(lpv[i][2]%lpv[i][1]):
        vacation += lpv[i][2]%lpv[i][1]
    else:
        vacation+=lpv[i][0]

    print('Case %d:'%(i+1),vacation)