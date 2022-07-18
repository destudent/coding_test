n = int(input())
arr=[]

for i in range(n):
    arr.append(int(input()))

arr.sort()

for i in range(1,n):
    arr[i] = arr[i-1]+arr[i]

result=0
for i in range(1,n):
    result+=arr[i]


if n !=0:
    print(result)
else:
    print(0)

# 30
# 40 70 (30+40)
# 50 120 (70+50)
# 100 220 (120+100)