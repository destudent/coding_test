n = int(input())

round_1 = list(map(int,input().split()))
round_2 = list(map(int,input().split()))

round_1_max=0
round_2_min=0

for i in range(n): 
    round_1_max+=abs(round_1[i])
    round_2_min+=abs(round_2[i])

print(round_1_max+round_2_min)