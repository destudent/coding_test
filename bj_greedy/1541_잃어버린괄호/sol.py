arr = input().split('-')
s = 0
for i in arr[0].split('+'):
    s += int(i)
#첫번째숫자더미에 +를 전부 더해주는 것. 맨처음 숫자는 무조건 +부호이고,
#split이 되지 않았다면 첫번째 숫자더미는 모두 덧셈으로 이뤄져있기 때문임.


for i in arr[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)
