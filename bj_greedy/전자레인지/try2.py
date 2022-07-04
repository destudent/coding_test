t = int(input())
a = 0
b= 0
c =0

if t % 10 == 0 :
    
    if t // 300 != 0:
        a = t//300
        t -= a*300
    if t // 60 != 0:
        b = t//60
        t -= b *60
    if t // 10 != 0:
        c = t //10
        t -= c *10


    print(a,b,c)
    
else:
    print('-1')

