n = int(input())
arr = list(map(int,input().split()))
arr.append(int(100001))

count= 0
count_max = 0

for i in range(n):
    if arr[i] > arr[i+1]:
        arr[i+1]=arr[i] #오른쪽방향으로 비교를 계속 하기위해 삽입
        count+=1

    else:
        count_max=max(count,count_max) # 비교해서 큰거 남기기
        count=0 # count 초기화
print(count_max)
