# N-Queen
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 10 초	128 MB	62230	30739	20167	48.767%
# 문제
# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 N이 주어진다. (1 ≤ N < 15)

# 출력
# 첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.


#1트 실패
#시간초과 - > pypy3
#https://seongonion.tistory.com/103

n = int(input())

ans = 0
row = [0] * n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i): #abs : 절댓값
            return False
    
    return True

def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return

    else:
        for i in range(n):
            # [x, i]에 퀸을 놓겠다.
            row[x] = i
            if is_promising(x):#대각선과 행(열)에 겹치지 않는다면
                n_queens(x+1)

n_queens(0)
print(ans)