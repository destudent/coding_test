n = int(input())

arr = list(map(int,input().split()))
dp=[]
dp_len=[]

#역순으로 작은것을 배열에 넣기

for j in range(n-1,-1,-1):

    dp = []
    dp.append(arr[j])#=15
    a=1
    for i in range(j,-1,-1):
        print(j)
        if arr[i]<dp[a-1]:
            dp.append(arr[i])
            a+=1
    print(dp)
    dp_len.append(len(dp))


# print(dp)
print(dp_len)