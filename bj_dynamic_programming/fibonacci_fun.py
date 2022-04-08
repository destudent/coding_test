memoization=[]*100

# 피보나치 함수를 재귀함수로 구현 (Top-down DP)
def fibo(x):
    
    if x == 0:

        return 0
    elif x == 1:

        return 1
    # 이미 계산한 적 있으면 그대로 반환
    if memoization[x] != 0:
        return memoization[x]
    # 계산한 적 없으면 점화식에 따라 피보나치 결과 반환
    memoization[x] = fibo(x - 1) + fibo(x - 2)
    return memoization[x]


# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
dp = [0] * 100
dp[1] = 1
dp[2] = 1
n = 99

# 피보나치 수열 반복문으로 구현(Bottom-Up DP)
for i in range(3, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]

print(dp[n])




