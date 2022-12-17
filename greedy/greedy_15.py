import sys
input=sys.stdin.readline

N=int(input())
candidates=[int(input()) for _ in range(N)]

cnt=0

while candidates.index(max(candidates))!=0:
    candidates[candidates.index(max(candidates))]-=1
    candidates[0]+=1
    cnt+=1
for i in range(1, N):
    if(candidates[0]==candidates[i]):
        candidates[i]-=1
        candidates[0]+=1
        cnt+=1

print(cnt)

#최악의 경우에 시간 복잡도 O(N^2)인가?