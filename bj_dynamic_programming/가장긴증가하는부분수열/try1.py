# 가장 긴 증가하는 부분 수열
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 1 초	256 MB	103246	40591	26629	37.315%
# 문제
# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오.

# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

# 입력
# 첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

# 둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

# 출력
# 첫째 줄에 수열 A의 가장 긴 증가하는 부분 수열의 길이를 출력한다.


n = int(input())

arr = list(map(int,input().split()))
dp=[]
dp_len=[]



for j in range(0,n):
    dp = []
    dp.append(arr[j])
    a=1
    for i in range(j+1,n):
        print(i)
        if arr[i]>dp[a-1]:
            dp.append(arr[i])
            a+=1
            dp_len.append(dp)

            print(dp)

# print(dp)
print(dp_len)