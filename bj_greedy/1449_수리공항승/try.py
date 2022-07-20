N,L = map(int,input().split())
leak=list(map(int,input().split()))

leak.sort()
#0.5만큼의 간격 ? = 각 센치미터 단위의 중앙에 위치하여한다는 뜻
tape=1
dist=0#구멍간의 거리
for i in range(1,N):
    dist +=abs(leak[i]-leak[i-1]) 
    if L > dist:
        #0.5센티미터의 간격이기 때문에 같아서는 안된다. 같게되면
        #각 테이프의 끝자락에 물이셀것임
        
        continue
    else:
        tape+=1
        dist=0
print(tape)