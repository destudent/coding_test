n,m=map(int,input().split())
arr=list(map(int,input().split()))

arr_sum=0

for i in range(m):
    arr.sort()
    arr_sum= arr[0]+arr[1]
    arr[0]=arr_sum
    arr[1]=arr_sum

print(sum(arr))