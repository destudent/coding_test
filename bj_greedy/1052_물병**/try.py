N,K = map(int,input().split())
water=1
bottle=0
while N!=K:
    
    if N % 2==1:
        N+=1
        bottle+=water
    else:
        N//=2
        water*=2
    print(N,K,water,bottle)
    if N<K:
        N=K
        bottle+=(K-N)*water

print(bottle)
    
# 13 14  7  8  4  2

# 1   1  2  2 

#     1     2  =3