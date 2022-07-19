A,B = map(int,input().split())
cnt=0
while B!=A:
    cnt+=1
    temp=B
    if B%10==1:
        B//=10

    elif B%2 ==0:
        B=B//2
        
    
    
    if B==temp:#변화가 없다면
        print('-1')
        break

else:
    print(cnt+1)