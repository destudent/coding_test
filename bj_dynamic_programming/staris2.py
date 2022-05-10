# #https://sungmin-joo.tistory.com/18
# import sys
# input = sys.stdin.readline
# arr =[] # 각 층별 값
# dp = [] # 해당 층 까지의 가장 큰 값

# l = int(input())

# for _ in range(l):
#     arr.append(int(input()))

# dp.append(arr[0]) # 0번째 까지의 최댓값
# dp.append(max(arr[0]+arr[1],arr[1])) # 1번째 까지의 최댓값
# dp.append(max(arr[0]+arr[2],arr[1]+arr[2])) # 2번째까지의 최댓값
# # 0번째+2번째가 큰가? 1번째+2번째가 큰가?

# if l ==1 :
#     print(arr[l])
# else:
#     for i in range(3,l): #2까지 미리 작성되어있기에 3부터
#         dp.append(max(dp[i-2]+arr[i],dp[i-3]+arr[i-1]+arr[i]))
# print(dp.pop())
# https://myjamong.tistory.com/311
import sys
read = sys.stdin.readline

n = int(read())
stairs = [0] + [int(read()) for _ in range(n)] + [0]
cache = [0] * (n+2)
cache[1] = stairs[1]
cache[2] = cache[1] + stairs[2]

for i in range(3, n+1):
    cache[i] = max(cache[i-2], cache[i-3] + stairs[i-1]) + stairs[i]
print(cache[n])