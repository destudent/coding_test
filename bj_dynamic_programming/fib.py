# 피보나치 함수
# 시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
# 0.25 초 (추가 시간 없음)	128 MB	154428	43960	34272	31.277%
# 문제
# 다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.

# int fibonacci(int n) {
#     if (n == 0) {
#         printf("0");
#         return 0;
#     } else if (n == 1) {
#         printf("1");
#         return 1;
#     } else {
#         return fibonacci(n‐1) + fibonacci(n‐2);
#     }
# }
# fibonacci(3)을 호출하면 다음과 같은 일이 일어난다.

# fibonacci(3)은 fibonacci(2)와 fibonacci(1) (첫 번째 호출)을 호출한다.
# fibonacci(2)는 fibonacci(1) (두 번째 호출)과 fibonacci(0)을 호출한다.
# 두 번째 호출한 fibonacci(1)은 1을 출력하고 1을 리턴한다.
# fibonacci(0)은 0을 출력하고, 0을 리턴한다.
# fibonacci(2)는 fibonacci(1)과 fibonacci(0)의 결과를 얻고, 1을 리턴한다.
# 첫 번째 호출한 fibonacci(1)은 1을 출력하고, 1을 리턴한다.
# fibonacci(3)은 fibonacci(2)와 fibonacci(1)의 결과를 얻고, 2를 리턴한다.
# 1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, fibonacci(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.

# 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.

# 출력
# 각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.



#top down 방식으로 했더니 시간초과 (내머리에서나옴)
number_0=0
number_1=0
numbers=[[]]

def fib(n):
    global number_0
    global number_1
    if n == 0:
        number_0+=1
        return 0
    elif n == 1 :
        number_1+=1
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n=int(input())
ans=[]
for i in range(n):
    ans.append(int(input()))

for i in ans:
    fib(i)
    print(number_0,number_1)
    number_0=0
    number_1=0
    




#solution 참고:https://jiwon-coding.tistory.com/28
# t = int(input())
 
# for _ in range(t):
#     cnt_0 = [1,0]
#     cnt_1 = [0,1]
#     n = int(input())
#     if n>1:
#         for i in range(n-1):
#             cnt_0.append(cnt_1[-1])#이전 cnt_1에서 더해짐. 0의 갯수는 이전 1의 갯수
#             cnt_1.append(cnt_0[-2]+cnt_1[-1]) #cnt_1의 갯수는 이전0+이전1의 갯수
 
#     print(cnt_0[n], cnt_1[n])
