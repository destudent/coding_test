n=int(input())
arr = list(map(int,input().split()))

arr.sort()

money=0
for i in range(1,n+1):
    money+=sum(arr[:i])


print(money)