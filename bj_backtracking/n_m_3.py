n,m = map(int,input().split())
s =[]


def dfs():
    
    if len(s)==m:

       
        print(' '.join(map(str,s)))
        

        return 
    
    for i in range(1,n+1):
        
            s.append(i) #가장 처음 1이 들어감 그다음 2,3,4... 
            dfs()
            s.pop() #리스트의 맨 마지막 요소를 제함
            
            
 
dfs()