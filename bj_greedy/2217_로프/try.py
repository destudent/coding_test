n = int(input())
rope=[]

for i in range(n):
    rope.append(int(input()))

rope.sort()
result=0


for i in range(0,n):
    result = max(rope[i]*(n-i),result)
    
print(result)