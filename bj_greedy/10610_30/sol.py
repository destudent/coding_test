n = input()
n = sorted(n, reverse=True)
sum = 0
if '0' not in n:	# 우선은 input의 디폴트인 string으로 받았기에 '0' 문자로 적음
    print(-1)
else:
    for i in n:

        sum += int(i)
    if sum % 3 != 0 :	# 3의 배수 체크
        print(-1)
    else :
        print(''.join(n))

# 30의 배수가 되는 조건

# - 일의 자리수가 0이여야 함.

# - 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야함.

# - 위 조건들을 통과한다면 그냥 내림차순으로 숫자들을 정렬한 숫자는 30의 배수이며 최댓값임.