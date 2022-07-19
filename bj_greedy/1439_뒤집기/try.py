S=input()


cnt=0
a=S[0]
for i in S:
    if a!=i:
        cnt+=1
        a=i

print((cnt+1)//2)