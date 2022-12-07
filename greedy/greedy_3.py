N,K=map(int, input().split())
coins=[int(input()) for _ in range(N)]
count=0

for i in reversed(range(N)):
    # 이 if 조건식은 결과 값에 영향을 미치지는 않지만 아래 과정을 줄여주지 않을까
    # 해서 작성해보았다.
    if(K>=coins[i]): 
        count+=K//coins[i]
        K%=coins[i]
    
print(count)
   