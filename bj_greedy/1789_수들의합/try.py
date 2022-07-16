#n은 갯수이기 때문에 최대로 하려면 1부터 시작해야함

s=int(input())

n=0
total=0
while 1:
    n=n+1
    total+=n
    if total>s:
        break

print(n-1)
#-1을 하는 이유는 total이 s를 넘어간 후를 조건으로 하기 때문에 
#그 직전인 -1을 해주는것