# https://velog.io/@bye9/%EB%B0%B1%EC%A4%80%ED%8C%8C%EC%9D%B4%EC%8D%AC-1932-%EC%A0%95%EC%88%98-%EC%82%BC%EA%B0%81%ED%98%95


n = int(input())
component= []


for i in range(n):
    component.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(component[i])):
        if j == 0 :
            component[i][j] = component[i][j]+component[i-1][j]
        elif j == len(component[i])-1:
            component[i][j] = component[i][j]+component[i-1][j-1]
        else :
            component[i][j] = max(component[i-1][j],component[i-1][j-1])+component[i][j]
print(max(component[n-1]))