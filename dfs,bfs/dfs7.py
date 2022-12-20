import sys
# 재귀함수 런타임 에러를 받지 않기 위해 제한해줌
sys.setrecusionlimit(10**6)
input=sys.stdin.readline

dx=[-1,1,0,0,-1,1,-1,1]
dy=[0,0,-1,1,-1,1,1,-1]

while True:
    w,h=map(int, input().split())
    if w==0 and h==0 : break

    land=[list(map(int, input().split())) for _ in range(h)]

    def dfs(x,y):
        if x<0 or x>=h or y<0 or y>=w:
            return False
        
        if land[x][y]==1:
            #방문처리
            land[x][y]=0
            for i in range(8):
                dfs(x+dx[i], y+dy[i])
            return True
        return False

    count=0

    for i in range(h):
        for j in range(w):
            if dfs(i,j)==True:
                count+=1
    print(count)

# 섬의 개수 (실버2)
# 기본적인 dfs 문제이지만
# 하나 다른것이 있다면 상하좌우대각선을 모두 dfs 처리 해줘야한다는 것.
# dx dy 범위를 늘려줌