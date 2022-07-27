from sys import stdin


t = int(stdin.readline())

for _ in range(t):
    n = int(stdin.readline())
    heights = [int(x) for x in stdin.readline().split()]
    heights.sort()

    max_level = 0
    for i in range(2, n):
        max_level = max(max_level, abs(heights[i] - heights[i - 2]))

    print(max_level)

# 문제는 통나무를 줄세우는게 아니라, 통나무를 줄세울 때 나오는 연산을 출력하고 차이의 최대값을 보는것이다.
#정렬한다음 2씩 차이나는 연산을 진행하는것이 키 포인트