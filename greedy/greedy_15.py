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

# candidates[0]=다솜 : 변수 하나를 굳이 새로 쓰고 싶지 않아서 그대로 사용함
# 득표수가 가장 많은 후보자의 표를 다솜이에게 주는 방식
# 다솜이가 후보자들 중 최고 득표수가 될때까지(while) 위 로직을 반복
# 여기까지 하면 max 특성상 동률을 제거하지 못함
# for 문을 사용해서 다솜이만 최대가 되게 변경해줌
