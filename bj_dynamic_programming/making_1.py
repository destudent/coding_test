# 1로만들기

# 정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

# X가 3으로 나누어 떨어지면, 3으로 나눈다.
# X가 2로 나누어 떨어지면, 2로 나눈다.
# 1을 뺀다.
# 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# 입력
# 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# 출력
# 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

n = int(input())

dp =[]
count = 0



def logic_1(count,dp):
    
    while dp[count-1]-1 : # n이 1이되면 종료하도록

        if dp[count-1]% 2 == 0 and dp[count-1]% 3 == 0:
            dp.append(dp[count-1]/3)
            count+=1
            
        elif dp[count-1]% 2 ==0:
            dp.append(dp[count-1]/2)
            count+=1
        elif  dp[count-1]% 3 ==0:
            dp.append(dp[count-1]/3)   
            count+=1
        else:
            dp.append(dp[count-1]-1)
            count+=1

    return count 

if n > 1:
    if((n-2)%3==0 and n % 12 ==0):
        dp.append(min((n-2)/3,n/12))
        count +=1

        ans=logic_1(count,dp)+2 ##세단계를 하는데 count는 한번만 더햊비니까
    elif ((n-2)%3==0 and n % 8 ==0):
        dp.append(min((n-2)/3,n/8))
        count +=1

        ans=logic_1(count,dp)+2
    elif (n-2)%3 == 0:

        dp.append(n-1)
        count+=1
        dp.append(dp[count-1]-1)
        count+=1
        dp.append((dp[count-1])/3)
        count+=1
        ans=logic_1(count,dp)
    elif (n-1)%3 == 0 and n%4 ==0:
        
        dp.append(min((n-1)/3,n/4))
        count +=1
        ans=logic_1(count,dp)+1 ##두단계를 하는데 count는 한번만 더햊비니까
    elif n%3 ==0 :
        
        dp.append(n/3)
        count+=1
        ans=logic_1(count,dp)
        

    elif (n-1)%3 == 0:
        
        
        
        dp.append((n-1))
        count+=1
        dp.append((dp[count-1])/3)
        count+=1
        ans=logic_1(count,dp)
    elif n%2 ==0:
        dp.append(n/2)
        count+=1
        ans=logic_1(count,dp)

    else :
        dp.append(n-1)
        count+=1
        ans=logic_1(count,dp)
else:
    ans = 0
print(ans)

   