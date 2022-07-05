n = int(input())
C = []
change =  [[0 for _ in range(4)] for _ in range(n)]

for i in range(n):
    C.append(int(input()))

for i in range(n):
    if C[i] // 25:
        change[i][0] = C[i]//25
        C[i] -= change[i][0]*25
    if C[i] // 10:
        change[i][1] = C[i]//10
        C[i] -= change[i][1]*10
    if C[i] // 5:
        change[i][2] = C[i]//5
        C[i] -= change[i][2]*5
    change[i][3] = C[i]
    
for i in range(n):
    print(change[i][0],change[i][1],change[i][2],change[i][3])

