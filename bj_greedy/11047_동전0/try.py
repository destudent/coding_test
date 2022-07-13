n,k = map(int,input().split())
coin = []
coin_index=0
time=0

for i in range(n):
    coin.append(int(input()))

while k :
    coin_min=100000000
    for i in range(n):
        if k//coin[i]<coin_min  :
            coin_min=k//coin[i] #coin_min이 0이 되기 전 coin
            if coin_min==0 :
                coin_index=i-1
            print(coin_min,'coin_min')
            print(coin_index,'coin_index')
    time+= k//coin[coin_index]
    k = k%coin[coin_index]

print(time)