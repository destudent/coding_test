n = int(input())

milk = list(map(int,input().split()))

sequence = 0 #순서를 나타냄
count = 0

for i in range(n):
    
    if milk[i]==0 and sequence == 0:
        count+=1
        sequence+=1
    if milk[i]==1 and sequence == 1:
        count+=1
        sequence+=1
    if milk[i]==2 and sequence == 2:
        count+=1
        sequence=0

print(count)