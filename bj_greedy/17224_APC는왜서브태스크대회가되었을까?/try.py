# 쉬운 버전과 어려운 버전으로 나누어 쉬운 버전만 맞더라도 부분점수를 주는 서브태스크 문제로 대회를 구성하는 것이다. 
# 또한 이렇게 만들어진 문제를 쉬운 버전의 난이도순으로 배치하려 한다.

n,l,k = map(int,input().split())
task = []
score_0=0
score_100=0
score_140=0

for i in range(n):
    task.append(list(map(int,input().split())))

for i in range(n):
    if task[i][1]<=l: #어려운 버전보다 역량이 높다면
        score_140+=1
    elif task[i][0]<=l and l < task[i][1]:
        #어려운 버전보다 작고 쉬운버전보다 역량이 높다면
        score_100+=1
    else:#둘보다 작으면
        score_0+=1

#k숫자에서 최대한 2를 많이 뽑고, 나머지를 1을 뽑는게좋음


if score_140-k>=0:
    print(k*140)
elif score_140-k<0 and score_140+ score_100-k>=0:
    print(140*score_140+100*(k-score_140))
elif score_140+score_100-k<0:
    print(140*score_140+100*score_100)
