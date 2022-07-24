n=int(input())
l=[int(input()) for i in range(n)]
c=0
for i in range(n-1,0,-1):
    x=max(l[i-1]-l[i]+1,0)
    c+=x
    l[i-1]-=x
print(c)