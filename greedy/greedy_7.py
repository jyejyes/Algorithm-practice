# 시간 복잡도 : O(n^2)
# 맞았지만 시간 복잡도를 줄이고 문제를 풀 수 있는 방법이 있을텐데 고민해봐야겠다

import sys
input=sys.stdin.readline

N=int(input())
P=list(map(int, input().split()))
total=0

P.sort()

for i in range(N):
    for j in range(i+1):
        total+=P[j]

print(total)


# 시간복잡도 : O(N)
# 검증 시간도 1/2 이상 효과가 있었음

import sys
input=sys.stdin.readline

N=int(input())
P=list(map(int, input().split()))
time=0
total=0

P.sort()

for i in range(N):
    time+=P[i]
    total+=time

print(total)