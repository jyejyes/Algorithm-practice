T=int(input())

#x,y 플마
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    if x<0 or x>=m or y<0 or y>=n:
        return False
    if matrix[x][y]==1:
        matrix[x][y]=0
        for i in range(4):
            dfs(x+dx[i], y+dy[i])
        return True
    return False

for i in range(T):
    m,n,k=map(int, input().split())
    spots=[list(map(int,input().split())) for _ in range(k)]

    # 빈 행렬
    matrix=[[0]*n for _ in range(m)]

    # 인접행렬 제작
    for spot in spots:
        a,b=spot
        matrix[a][b]=1

    count=0

    for i in range(m):
        for j in range(n):
            if dfs(i,j)==True:
                count+=1

    print(count)

# 유기농 배추(실버2)
# 테스트 케이스만큼 반복
# 처음에 빈 행렬을 만들어주고 주어진 케이스로 인접행렬 제작해줌
# 그 뒤 dfs 사용
# 백준에서는 런타임 에러나는데 구동 시 오류는 없음
