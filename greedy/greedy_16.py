import sys
input=sys.stdin.readline

N=int(input())

A=list(map(int, input().split()))
B=list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

min_total=0

for i in range(N):
    min_total+=A[i]*B[i]

print(min_total)

# 보물 (실버4)
# 각각의 배열 오름차순, 내림차순으로 정렬한 후 함수 계산을 해주면 
# 합이 가장 최소가 됨