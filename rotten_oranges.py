from collections import deque

n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
q=deque()
fresh=0
for i in range(n):
    for j in range(m):
        if a[i][j]==2:
            q.append((i,j))
        elif a[i][j]==1:
            fresh+=1
time=0
d=[(-1,0),(1,0),(0,-1),(0,1)]
while q and fresh:
    for _ in range(len(q)):
        x,y=q.popleft()
        for dx,dy in d:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and a[nx][ny]==1:
                a[nx][ny]=2
                fresh-=1
                q.append((nx,ny))
    time+=1
print(time if fresh==0 else -1)
