import sys
input=sys.stdin.readline
S=int(input())

N,cnt=1,0

while S>=N:
    S-=N
    cnt+=1
    N+=1    
print(cnt)