# 실패사유 : 함수 안에 재귀를 실행할 때 for문으로 감쌌음. 
# 그럼 인덱스가 초기화됨

n = int(input())
number_list = list(map(int,input().split()))
plus,minus,mul,div = map(int,input().split())
sub_result=[]
result=[]
def oper(index,plus,minus,mul,div):

    for i in range(len(number_list)):
        ## 숫자 사이에 연산자가 들어감. 즉 n-1 = 연산자 수
        if index+1==n:# index+1을 해야 재귀되며 end타이밍이 맞음.
            print(sub_result)
            
            return

        if i == 0:
            sub_result.append(number_list[i])
            continue
        
        if plus != 0:
            sub_result.append(sub_result[i-1]+number_list[i])#1부터 시작
            plus-=1
            print("plus : ",plus)
            print("sub_result : ",(sub_result[i-1]+number_list[i]))
            index+=1
            oper(index,plus,minus,mul,div)
            # plus+=1
            sub_result.pop()
        if minus != 0:
            sub_result.append(sub_result[i-1]-number_list[i])#1부터 시작
            minus-=1
            print("minus : ",minus)
            print("sub_result : ",(sub_result[i-1]-number_list[i]))
            index+=1
            oper(index,plus,minus,mul,div)
            # minus+=1
            sub_result.pop()
        if mul != 0:
            sub_result.append(sub_result[i-1]*number_list[i])#1부터 시작
            mul-=1
            print("mul : ",mul)
            print("sub_result : ",(sub_result[i-1]*number_list[i]))
            index+=1
            oper(index,plus,minus,mul,div)
            # mul +=1
            sub_result.pop()
        if div != 0:
            sub_result.append(sub_result[i-1]/number_list[i])#1부터 시작
            div-=1
            print("div : ",div)
            print("sub_result : ",(sub_result[i-1]/number_list[i]))
            index+=1
            oper(index,plus,minus,mul,div)
            # div+=1
            sub_result.pop()

oper(0,plus,minus,mul,div)
        
        
        
        

