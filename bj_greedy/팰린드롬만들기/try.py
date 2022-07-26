
arr = input()
arr_cnt=[0 for _ in range(26)]
for a in arr: #알파벳만큼의 길이를 생성한 후, 배열에 저장
    arr_cnt[ord(a)-65]+=1

odd = 0
odd_alphabet = ''
alphabet=''

for i in range(26):
    if arr_cnt[i]%2 == 1: #저장된 갯수가 홀수이면
        odd+=1 
        odd_alphabet+= chr(i+65) #홀수만 모아놓은 배열에wjwkd
    alphabet+=chr(i+65)*(arr_cnt[i]//2)

if odd>1: #만약 홀수가 두개 이상이면 팰린드롬 못만듦 (가운데에 하나만 있어야 하므로)
    print("I'm Sorry Hansoo")
else:
    print(alphabet+odd_alphabet+alphabet[::-1])
