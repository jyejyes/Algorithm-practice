import sys
input=sys.stdin.readline

N=int(input())
ropes=[int(input()) for _ in range(N)]

ropes.sort(reverse=True)

for i in range(N):
    ropes[i]*=(i+1)
print(max(ropes))
    

