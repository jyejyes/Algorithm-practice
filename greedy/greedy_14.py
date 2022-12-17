import sys
input=sys.stdin.readline

N=int(input())
T=list(map(int, input().split()))

T.sort(reverse=True)

for i in range(N):
    T[i]-=N-(i+1)

print(1+N+max(T))

# 1. 시간이 오래 걸리는 것을 먼저 심어야 해서 내림차순 정렬
# 2. for 문을 통해 N일(모든 묘목 심는 시간) 뒤 남은 시간을 구해주고
# 3. 1(묘목 산 날)+N(묘목 심은 날)+남은 시간이 가장 많이 남은 일 수 더해서 출력