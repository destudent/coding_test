n = int(input())

dp = [0] * 101
dp_0 = [0]* 101
dp_9 = [0]* 101

dp[1]=9
dp[2]=15

dp_0[1]=1
dp_0[2]=1

dp_9[1]=1
dp_9[2]=1

for i in range(3,n+1):
    if i % 2 ==1: #홀수
        dp_9[i]=dp_9[i-1]*3
    else:
        dp_9[i]=dp[i-1]
    if i % 2 == 0: #짝수
        dp_0[i]=dp_0[i-1]*3
    else:
        dp_0[i]=dp_0[i-1]
    dp[i]=(dp[i-1]*2-1+dp_0[i]+dp_9[i])%1000000000

print(dp[n])
