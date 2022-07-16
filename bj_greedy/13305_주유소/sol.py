n= int(input())
kilo = list(map(int,input().split()))
price = list(map(int,input().split()))

res = 0
m=price[0]

for i in range(n-1):
    if price[i]<m:
        m=price[i]
    res+= m*kilo[i]
print(res)

# 92
# 7*8 5*2 4*2 2*9