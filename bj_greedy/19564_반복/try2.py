arr= input()

alphabet='abcdefghijklmnopqrstuvwxyz'
time=0
seq=0

for i in alphabet:
    for j in arr:
        if i==arr[seq]:
            time+=1
            seq+=1
print(time)