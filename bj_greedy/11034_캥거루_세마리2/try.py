
while 1:
    try:
        a,b,c = map(int,input().split())
        jump = max(b-a-1,c-b-1)

        print(jump)
    except:
        exit()