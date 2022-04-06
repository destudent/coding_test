#참고 :https://www.acmicpc.net/problem/2580


sudoku=[]
index_0=[]

for i in range(9):
 sudoku.append(list(map(int,input().split())))



for i in range(9):#0탐색함. 이거 참고함..
    for j in range(9):
        if sudoku[i][j]==0:
            index_0.append((i,j))

def row(r,a):#r값
    for i in range(9):
        if a ==sudoku[r][i] :#포함되어 있다면(0이 아니라면)
            return False
        
    return True

def col(l,a):
    for i in range(9):
        if a ==sudoku[i][l] :
            return False

    return True

def rule_3x3(r,l,a):#이부분은 살짝 참고함

    dx = r//3 *3 #몫을 3으로 나누고, 3을 곱하면 시작점을 알 수 있다.
    dy = l //3 *3
    for i in range(3):
        for j in range(3):
            if a ==sudoku[dx+i][dy+j]:
                return False
    
    return True

def dfs(idx):
    if idx == len(index_0):
        for i in range(9):
            print(*sudoku[i])
        exit(0)

    for i in range(1,10):
        x = index_0[idx][0]
        y = index_0[idx][1]
        if row(x,i) and col(y,i) and rule_3x3(x,y,i):
            sudoku[x][y] = i
            dfs(idx+1) # 다음 0의 위치를 소환함
            sudoku[x][y]=0 #다시 0을 넣어 줌으로써




dfs(0)

    

        
