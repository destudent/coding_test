#연산자 끼워넣기

# 문제
# N개의 수로 이루어진 수열 A1, A2, ..., AN이 주어진다. 또, 수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어진다. 연산자는 덧셈(+), 뺄셈(-), 곱셈(×), 나눗셈(÷)으로만 이루어져 있다.

# 우리는 수와 수 사이에 연산자를 하나씩 넣어서, 수식을 하나 만들 수 있다. 이때, 주어진 수의 순서를 바꾸면 안 된다.

# 예를 들어, 6개의 수로 이루어진 수열이 1, 2, 3, 4, 5, 6이고, 주어진 연산자가 덧셈(+) 2개, 뺄셈(-) 1개, 곱셈(×) 1개, 나눗셈(÷) 1개인 경우에는 총 60가지의 식을 만들 수 있다. 예를 들어, 아래와 같은 식을 만들 수 있다.

# 1+2+3-4×5÷6
# 1÷2+3+4-5×6
# 1+2÷3×4-5+6
# 1÷2×3-4+5+6
# 식의 계산은 연산자 우선 순위를 무시하고 앞에서부터 진행해야 한다. 또, 나눗셈은 정수 나눗셈으로 몫만 취한다. 음수를 양수로 나눌 때는 C++14의 기준을 따른다. 즉, 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꾼 것과 같다. 이에 따라서, 위의 식 4개의 결과를 계산해보면 아래와 같다.

# 1+2+3-4×5÷6 = 1
# 1÷2+3+4-5×6 = 12
# 1+2÷3×4-5+6 = 5
# 1÷2×3-4+5+6 = 7
# N개의 수와 N-1개의 연산자가 주어졌을 때, 만들 수 있는 식의 결과가 최대인 것과 최소인 것을 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 수의 개수 N(2 ≤ N ≤ 11)가 주어진다. 둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 100) 셋째 줄에는 합이 N-1인 4개의 정수가 주어지는데, 차례대로 덧셈(+)의 개수, 뺄셈(-)의 개수, 곱셈(×)의 개수, 나눗셈(÷)의 개수이다. 

# 출력
# 첫째 줄에 만들 수 있는 식의 결과의 최댓값을, 둘째 줄에는 최솟값을 출력한다. 연산자를 어떻게 끼워넣어도 항상 -10억보다 크거나 같고, 10억보다 작거나 같은 결과가 나오는 입력만 주어진다. 또한, 앞에서부터 계산했을 때, 중간에 계산되는 식의 결과도 항상 -10억보다 크거나 같고, 10억보다 작거나 같다.

# 예제 입력 1 
# 2
# 5 6
# 0 0 1 0
# 예제 출력 1 
# 30
# 30

import numbers


n = int(input())
a_n = list(map(int,input().split()))
operator = list(map(int,input().split()))
cal=[]
result_numbers=[]




def plus(a,b,i):
    a[i] = a[i]+b
    return 
def minus(a,b,i):
    a[i] = a[i]-b
    return 
def mul(a,b,i):
    a[i] = a[i]*b
    return 
def divide(a,b,i):
    a[i] = a[i]/b
    return 

def oper(index):
    if index == 0:
        cal.append(a_n[0])
        return
    
    for i in range(1,len(a_n)):


        if operator[0]!=0: #add
            plus(cal[i-1],a_n[i],i)#이전것과 이번것 더하기
            print(cal[i])##
            b = cal[i]
            operator[0]=b-1
            oper(index+1)
            cal[i]=0
        if operator[1]!=0: #minus
            minus(cal[i-1],a_n[i],i)#이전것과 이번것 더하기
            print(cal[i])##
            b = cal[i]
            operator[0]=b-1
            oper(index+1)
            cal[i]=0
        if operator[2]!=0: #mul
            mul(cal[i-1],a_n[i],i)#이전것과 이번것 더하기
            print(cal[i])##
            b = cal[i]
            operator[0]=b-1
            oper(index+1)
            cal[i]=0
        if operator[3]!=0: #divide
            divide(cal[i-1],a_n[i],i)#이전것과 이번것 더하기
            print(cal[i])##
            b = cal[i]
            operator[0]=b-1
            oper(index+1)
            cal[i]=0

            
        print(cal[i])
        if len(cal) == n:
            result_numbers.append(cal[i])
            print(result_numbers)  
            return 

oper(0)
# print(a_n)
# print(operator)
# print(cal)
