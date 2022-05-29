
n , k =map( int,input().split())
arr = list(map(int,input().split()))

sum_list = []

for i in range(n-k+1):
    sum_list.append(sum(arr[n:n+k]))

print(sum)