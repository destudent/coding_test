arr = input()
alphabet='abcdefghijklmnopqrstuvwxyz'
seq=0
time=0
arr_break=0

for i in range(len(arr)-1):
    for j in range(len(alphabet)):

        if seq==len(arr):
            print(time)
            arr_break=1

        if alphabet[j]==arr[seq]:
            seq+=1



    time+=1

