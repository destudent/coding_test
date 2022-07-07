
ZOAC = input()
check = 0#초깃값 A
time = 0
for i in range(len(ZOAC)):
    tmp = ord(ZOAC[i])-65
    time += min(abs(tmp-check),26-abs(tmp-check))
    check=tmp
print(time)