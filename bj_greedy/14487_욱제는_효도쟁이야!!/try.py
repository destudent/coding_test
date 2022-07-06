n = int(input())
town = list(map(int,input().split()))

#모든 마을을 다 돌아야함
#방향은 상관 없음

#가장 비싼 마을에서 시작해서 왼쪽으로 가면 최소비용으로 
#전부 순회할 수 있음

cost = sum(town)

cost -= max(town)

print(cost)