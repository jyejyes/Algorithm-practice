N=list(map(int, input()))
N.sort(reverse=True)

# 일반 if 문 사용
if(N[-1]==0 and sum(N)%3==0):
    print(''.join(map(str, N)))
else:
    print(-1)
    
# 삼항 연산자 사용
print(''.join(map(str, N))) if N[-1]==0 and sum(N)%3==0 else print(-1)

# 조건 1) 0이 존재해야함
# 조건 2) 1을 만족하면서 각 자릿수의 합이 3의 배수여야함

# join 사용법
# 구분자.join(합칠 리스트)
# a=[1,2,3,4]
# ex. ''.join(a) = 1234
# ex. ','.join(a) = 1,2,3,4