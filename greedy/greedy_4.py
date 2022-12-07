N,M,K=map(int, input().split())

for i in range(K):
    if N//2 < M : M-=1
    else: N-=1

print(min(N//2,M))


# 1. 여자는 2명이 나가야하므로 2로 나눈 몫으로 계산해줌 (홀수일 경우 내림)
# 2. N//2 과 M 값을 비교해서 값이 많은 쪽 사람 인원을 하나 빼주고 최종적으로 적은 수를 출력함

# 풀다 알게 된 파이썬의 희한한 삼항연산자 
# [true_value] if [condition] else [false_value]