# https://velog.io/@kimdukbae/BOJ-14888-%EC%97%B0%EC%82%B0%EC%9E%90-%EB%81%BC%EC%9B%8C%EB%84%A3%EA%B8%B0-Python
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9 
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N: # 특정 깊이에 도착하면 해당 값과 maxmum,minimum을 비교함. 
        #minimum은 엄청 크고, maximum은 엄청 작은 초깃값을 갖고있어서 해당값에 max와 min 을하여 값 도출

        maximum = max(total, maximum)
        minimum = min(total, minimum)
        # print(total)
        return

    if plus: #if 는 1 이상이면 다 괜찮다. 1=2=3 다같음 0만 아니면된다. 
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)