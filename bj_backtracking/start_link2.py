#for 문 써서 한명씩
#예를 들어서 n=6이면 array가 n/2가 될 때,
#넘어가고
#그 N/2의 모든 조합을 구하기


n = int(input())
member = []

for i in range(n):
    member.append(list(map(int,input().split())))

start =[]
link = []
stat=[]

def start_link():
    if len(start) == (n/2):#길이가 충족되었을 때 
        # print(start)
        # print(link)
        # print('----------')
        find_stat(start,link)
        return

    for i in range(n):
        for j in range(n):
            if i == j :
                continue
            #start와 link의 사람들의 경우의 수를 모두 뽑아냄
            if i not in start and  i not in link and j not in start and j not in link:
                start.append(i)
                link.append(j)
                start_link()
                start.pop()
                link.pop()

def find_stat(start,link): #각 팀의 점수 합계
    start_stat=0
    link_stat=0

    for i in range(len(start)):
        for j in range(len(start)):
            #완전탐색
            if start[i]!=start[j]:
               start_stat +=member[start[i]][start[j]]
            if link[i]!=link[j]:
                link_stat +=member[link[i]][link[j]]
            #점수가 다 나옴
    
    stat.append(abs(start_stat-link_stat))#점수의 차이 append
    



start_link()

print(min(stat))