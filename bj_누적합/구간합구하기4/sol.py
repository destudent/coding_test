# https://velog.io/@kimdukbae/BOJ-11659-%EA%B5%AC%EA%B0%84-%ED%95%A9-%EA%B5%AC%ED%95%98%EA%B8%B0-4-Python
import sys

input = sys.stdin.readline
n, m = map(int,input().split())
arr = list(map(int,input().split()))

sum_=0
sum_list=[0]


for i in range(n):
    sum_+=arr[i]
    sum_list.append(sum_)


for i in range(m):
    a,b = map(int,input().split())
    print(sum_list[b]-sum_list[a-1])
