n= int(input())
kilo = list(map(int,input().split()))
price = list(map(int,input().split()))

money=price[0]*kilo[0]

if min(price) == price[0]:
    print(sum(kilo)*price[0])
else:
    for i in range(1,n-1):#마지막도시에서는 기름살필요가없음
        if min(price[i:n-1])==price[i]:
            money+=price[i]*sum(kilo[i:])
            break

        else:
            money+=kilo[i]*price[i]

    print(money)
