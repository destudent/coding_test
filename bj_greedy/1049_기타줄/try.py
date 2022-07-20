n,m= map(int,input().split())
price=[]

for i in range(m):
    price.append(list(map(int,input().split())))

price_six=sorted(price,key= lambda x:(x[0]))
price_one=sorted(price,key= lambda x:(x[1]))

price_six_min=price_six[0][0]
price_one_min=price_one[0][1]

price_min=0

while n>0:
    if n>6: #6개보다 많다면
        if (price_one_min*6)>price_six_min:
            #여섯줄들은게 더 싸다면(한줄을 여섯개 사는것보다)
            price_min+=price_six_min*(n//6)
            #여섯줄이 들은걸 6의 배수로 사기
            n%=6
            #나머지
        else:
            #만약 한줄들은것이 여섯개들은것들의 최솟값보다 싸다면
            price_min+=price_one_min*n
            #그냥 다 사버리기
            n=0
    else:
        #여섯개 미만이라면
        if price_one_min*n>price_six_min:
            #한줄을 n개많큼 사는게 더 비싸면
            price_min+=price_six_min
            #그냥 여섯개 사버리기
            n=0
        else:
            #한줄을 n개만큼 사는게 더 싸다면
            price_min+=price_one_min*n
            #n개만큼 사기
            n=0

print(price_min)