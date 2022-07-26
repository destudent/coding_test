import sys
import heapq

number,repeat = map(int,sys.stdin.readline().split(' '))
inp = list(map(int,sys.stdin.readline().split(' ')))

heapq.heapify(inp) #정렬
sum = int(0)
answer = 0
for i in range(repeat):    
    sum=heapq.heappop(inp)+heapq.heappop(inp)
    heapq.heappush(inp, sum)
    heapq.heappush(inp, sum)

    
for k in range(number):
    answer = answer + inp[k]
print(answer)