#스타트와 링크

# 오늘은 스타트링크에 다니는 사람들이 모여서 축구를 해보려고 한다. 축구는 평일 오후에 하고 의무 참석도 아니다. 축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수이다. 이제 N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

# BOJ를 운영하는 회사 답게 사람에게 번호를 1부터 N까지로 배정했고, 아래와 같은 능력치를 조사했다. 능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치이다. 팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. Sij는 Sji와 다를 수도 있으며, i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치는 Sij와 Sji이다.

# 축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로 하려고 한다. 위의 예제와 같은 경우에는 1, 4번이 스타트 팀, 2, 3번 팀이 링크 팀에 속하면 스타트 팀의 능력치는 6, 링크 팀의 능력치는 6이 되어서 차이가 0이 되고 이 값이 최소이다.

# 입력
# 첫째 줄에 N(4 ≤ N ≤ 20, N은 짝수)이 주어진다. 둘째 줄부터 N개의 줄에 S가 주어진다. 각 줄은 N개의 수로 이루어져 있고, i번 줄의 j번째 수는 Sij 이다. Sii는 항상 0이고, 나머지 Sij는 1보다 크거나 같고, 100보다 작거나 같은 정수이다.

# 출력
# 첫째 줄에 스타트 팀과 링크 팀의 능력치의 차이의 최솟값을 출력한다.

#한명의 좌표를 먼저 구했고 쌍으로 다른사람의 좌표도 구함. -> n= 4일때는 가능함. but
#이게 잘못된 이유는 팀단위로 묶지 않았기 때문에
#팀의 점수를 환산할 수 없음

#결론은 팀의 배열로 for문을 돌려야함.


n = int(input())
member = []
index_0=[]
a =[]

row=[]
col=[]

for i in range(n):
    member.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if i == j :
            continue
        index_0.append((i,j))

def start_link():
    if len(row)==int(n/2):
        for i in range(len(row)):
            # print(row,col)
            # print(member[row[i]][col[i]],member[col[i]][row[i]])
            print(a)
            print('한팀')


        return
    # for i,j in index_0:
    #     #
    #     if (j,i) in a:
    #         continue
    #     a.append((i,j)) #중복 출력 방지용
    #     #
    #     print(member[i][j],member[j][i])
    for i,j in index_0:
        if (i not in row) and (i not in col) and (j not in row) and (j not in col):
        # if  (i not in col) and (j not in row) :
        # if  (j not in col) and (i not in row) :
            row.append(i)
            col.append(j)
            a.append((i,j))
            start_link()
            a.pop()
            row.pop()
            col.pop()

start_link()

