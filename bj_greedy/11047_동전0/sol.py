N, K = map(int, input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
coins.sort(reverse=True)

############
result=0
for i in coins:
    if K==0: 
      break
    result += K//i #안나워지면 0이나옴
    K %= i #k를 i로 나눴을 때 나머지를 k로 선언
    print(K,i)

print(result)
