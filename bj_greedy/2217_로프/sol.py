import sys
In = sys.stdin.readline

def main():
    n = int(In())
    rope = [0] * 10001 #rope array생성
    for _ in range(n):
        rope[int(In())] += 1 # 입력에 해당하는 번호에 1을 입력
        # 입력이 없는 배열은 0이 있어 곱셈을 해도 0이됨
    m, s = 0, 0
    for x in range(10000,-1,-1):
        s += rope[x]
        #내림차순으로 배열에 있는 모든 수를 곱하며 더함
        m = max(m, x * s)
    print(m)
main()