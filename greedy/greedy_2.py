# 끝나는 시간이 가장 이른 것을 기준으로 개수를 셈
# greedy 알고리즘 

N=int(input())
meetings=[list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x:(x[1],x[0])) # 끝나는 시간, 시작 시간 순으로 정렬
cnt, end = 1, meetings[0][1]

for i in range(N-1):
    if end<=meetings[i+1][0]:
        end=meetings[i+1][1]
        cnt+=1

print(cnt)
    

