# https://kyoung-jnn.tistory.com/entry/%EB%B0%B1%EC%A4%802565%EB%B2%88%ED%8C%8C%EC%9D%B4%EC%8D%ACPython-%EC%A0%84%EA%B9%83%EC%A4%84-DP
N = int(input())

lineList = []

for _ in range(N):
    lineList.append(list(map(int, input().split())))

lineList.sort()

dp = [1]*N
for i in range(N):
    for j in range(i):
        if lineList[i][1] > lineList[j][1] and dp[i] < dp[j]+1:
            dp[i] = dp[j] + 1

print(N-max(dp))