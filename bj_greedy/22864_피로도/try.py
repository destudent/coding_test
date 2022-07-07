a,b,c,m = map(int,input().split())

time=(m+24*c)//(a+c)

if time>24:
    time = 24

if a >m:
    print('0')
else:
    print(time*b)

print(time)