


n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

result=0
for i in range(n-1,0,-1):
    if arr[i-1]>=arr[i]:
        result+=arr[i-1]-arr[i]+1
        arr[i-1]-=arr[i-1]-arr[i]+1
print(result)