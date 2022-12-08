# 시간 복잡도 : O(N)
# A 주감독은 모든 강의실에 있어야 하므로 계산해줄건 B 부감독 밖에 없다.
# 맨처음 각 학생 수에서 A 가 감독할 수 있는 학생의 수를 빼고 시작한다. 
# A만큼 값이 빠진 테스트 값들을 b값으로 나눈 뒤 올림해주고(사람은 쪼갤 수 없으므로) b-cnt 값에 저장한다.

from math import ceil
import sys
input=sys.stdin.readline

N=int(input())
T=list(map(int, input().split())) 
A,B=map(int, input().split())

T=[x-A for x in T]

B_cnt=0

for i in range(N):
    if(T[i]>0):
        B_cnt+= ceil(T[i]/B)

print(N+B_cnt)