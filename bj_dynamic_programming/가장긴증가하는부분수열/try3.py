
n = int(input())

arr = list(map(int,input().split()))
dp=[]
dp_len=[]



# for i in range(0,n):
#     for j in range(i+1,n):
#         dp = []
#         dp.append(arr[j])
        
#         for k in range(j,n):

#             # if arr[k]>dp[a]:
#                 print('i: ',i,' j: ',j,' k:',k,' a:',a)
#                 dp.append(arr[k])
#                 a+=1
#             #     dp_len.append(dp)

#                 print(dp    )

# print(dp)

for i in range(0,n):
    dp = []
    dp.append(arr[i])
    for j in range(i+1,n):
        
        for k in range(j,n):
            print('i: ',i,' k:',k)
            if arr[k]>dp[i]:
                dp.append(arr[k])
            
        print(dp)