str=input().replace(' ','')
ucpc=['U','C','P','C']
idx=0
cnt=0

for i in str:
    if i==ucpc[idx]:
        cnt+=1
        idx+=1
    if cnt==4:
        break;

print('I love UCPC' if cnt==4 else 'I hate UCPC')