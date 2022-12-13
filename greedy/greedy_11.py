# 뒤집기 (실버 5)
# 시간 복잡도 : O(N)
# 숫자가 달라지는 구간들을 cnt 올려준 뒤 나누기 2 해줌
import math
S=list(input())

cnt=0

for i in range(len(S)-1):
    if(S[i]!=S[i+1]):
        cnt+=1
        
print(math.ceil(cnt/2))

#다른 풀이(찾아본 풀이)
S=list(input())
print(max(S.count('01'), S.count('10')))