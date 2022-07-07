a,b,c,m = map(int,input().split())

tired=0
work=0

for i in range(1,25):
    if tired + a <=m:
        tired+=a
        work+=b
    else:
        if tired-c>=0:
            tired-=c
        else:
            tired=0

if a>m:
    print('0')
else:
    print(work)