from collections import deque

n=int(input())
graph=[list(map(int, input())) for _ in range(n)]

def dfs(x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y]==1:
        global count
        count+=1

        # 방문 처리
        graph[x][y]=0
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        
        return True
    return False

count=0
count_arr=[]
result=0

for i in range(n):
    for j in range(n):
        if dfs(i, j)==True:
            count_arr.append(count)
            result+=1
            count=0

count_arr.sort() #오름차순으로 정렬
print(result)
for i in count_arr:
    print(i)


# 단지번호붙이기(실버1)
# dfs 로 탐색해주고 global count 값을 더해주고 초기화해주는 과정을 반복함.
# 마지막 print 는 오름차순 정렬 후 출력을 위해 조정 과정 필요