
text=input()
result=''
UCPC='UCPC'
UCPC_set=['U','P','C']
for i in range(len(text)):
    if ord(text[i])<=ord('Z') and ord(text[i]) >=ord('A'):

        result+=text[i]
UCPC_seq=0
err=0
for i in result:
    if i =='U' and UCPC_seq==0:
        UCPC_seq+=1
    if i =='C' and UCPC_seq==1:
        UCPC_seq+=1
    if i =='P' and UCPC_seq==2:
        UCPC_seq+=1
    if i=='C' and UCPC_seq==3:
        UCPC_seq+=1
    if i!='U' and i!='C' and i!='P':
        err+=1

if err>0 or UCPC_seq <4:
    print('I hate UCPC')
else:
    print('I love UCPC')