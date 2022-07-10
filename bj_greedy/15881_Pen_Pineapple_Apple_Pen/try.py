n = int(input())
arr = str(input())

count = 0
seq = 0

for i in range(n-3):

    if arr[i]=='p' :
        if arr[i+1]=='P':
            if arr[i+2]=='A':

                if arr[i+3]=='p' and (seq!=i or seq == 0):
#seq!=i는 p가 중복해서 겹치지 않도록 해준다. 일전에 pPAp세트와 겹친다면 i+3을 해 마지막 p의 순서를 저장함
# or seq ==0은 맨 처음 seq를 0으로 선언하기 때문에 예외케이스를 넣은것.
                    count+=1
                    seq = i+3


print(count)
    