#N과 M (2)
#시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
#1 초	512 MB	38251	28681	20923	74.515%
#문제
#자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

#1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
#고른 수열은 오름차순이어야 한다.
#입력
#첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)

#출력
#한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

#수열은 사전 순으로 증가하는 순서로 출력해야 한다. ###


n,m = map(int,input().split())
s =[]


def dfs(start):
    
    if len(s)==m:
        print(s)
       
        print(' '.join(map(str,s)))
        

        return 
    
    for i in range(start,n+1):
        if i not in s:
            s.append(i) #가장 처음 1이 들어감 그다음 2,3,4... 
            dfs(i+1)
            s.pop() #리스트의 맨 마지막 요소를 제함
            
            
 
dfs(1)
