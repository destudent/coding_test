word = input()
alphabet = 'abcdefghijklmnopqrstuvwxyz'
count = 1

for i in range(len(word)-1):
  if alphabet.index(word[i]) < alphabet.index(word[i+1]) :
#문자열의 index가 어딨는지 호출 후 비교함
#만약 word의 뒷글자가 후순이라면, count할 필요없음
    continue
  else :
    count += 1
    #더이상 count할 수 없을때 +1
print(count)

