import sys
sys.setrecursionlimit(100000)

n=int(input())
matrix=[list(map(int, input().split())) for _ in range(n)]

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(matrix, x,y):
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if matrix[x][y]==1:
        #방문 처리
        matrix[x][y]=0
        for i in range(4):
            dfs(matrix, x+dx[i], y+dy[i])
        return True
    return False

temp_matrix=[[0]*n for _ in range(n)]
count_arr=[]

for k in range(min(min(matrix))-1,max(max(matrix))):
    count=0

    for i in range(n):
        for j in range(n):
            if k<matrix[i][j]:
                temp_matrix[i][j]=1
            else : temp_matrix[i][j]=0

    for i in range(n):
        for j in range(n):
            if dfs(temp_matrix, i,j)==True:
                count+=1
    count_arr.append(count)
print(max(count_arr))

# 안전영역 (실버1)
# dfs 사용
# 입력받은 값들 중 min-1 부터 max 까지의 경우의 수를 찾아 그 중 최댓값을 출력해주었다.
# min-1 로 준 이유는 모두 같은 수준의 지대를 가지고 있을 수 있기 때문
# 0으로 주게되면 불필요한 연산이 많아지므로 min-1 부터 시작했다.
# 지역을 0과 1로 이루어진 인접 행렬로 바꾸는 작업을 거친 후 해당 행렬에 대해 dfs 를 수행해주었다.