# 실패사유 : 함수 안에 재귀를 실행할 때 for문으로 감쌌음. 
# 그럼 인덱스가 초기화됨

n = int(input())
number_list = list(map(int,input().split()))
operator = list(map(int,input().split()))
operator_a=operator
sub_result=[]
result=[]
def oper(index):
    ## 숫자 사이에 연산자가 들어감. 즉 n-1 = 연산자 수
    

    # if index == n:# index+1을 해야 재귀되며 end타이밍이 맞음.
    #         print(sub_result)
            
    #         return
    if index ==0:
        sub_result.append(number_list[index])
        index +=1 # subresult와 index 맞추기
    
    for i in range(len(operator)):
        # if index==n:# index+1을 해야 재귀되며 end타이밍이 맞음.
        #     print(sub_result)
            
        #     return

        # if operator[i] == operator_a
        print(index,'gkgk')
        print(sub_result)
        print(number_list)
        if i ==0:
            if operator[i] != 0:
                
                sub_result.append(sub_result[index-1]+number_list[index])
                operator[i] = operator[i]-1 #연산자 카운트 감소
                index+=1
                oper(index)
                # operator[i] = operator[i]+1
        if i ==1:
            if operator[i] != 0:
                sub_result.append(sub_result[index-1]-number_list[index])
                operator[i] = operator[i]-1 #연산자 카운트 감소
                index+=1
                oper(index)
                # operator[i] = operator[i]+1
    
        if i ==2:
            if operator[i] != 0:
                sub_result.append(sub_result[index-1]*number_list[index])
                operator[i] = operator[i]-1 #연산자 카운트 감소
                index+=1
                oper(index)
                # operator[i] = operator[i]+1
        if i ==3:
            if operator[i] != 0:
                sub_result.append(sub_result[index-1]/number_list[index])
                operator[i] = operator[i]-1 #연산자 카운트 감소
                index+=1
                oper(index)
                # operator[i] = operator[i]+1
        
oper(0)


        
        
        

