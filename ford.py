from collections import deque
v,e=map(int,input().split())
g=[[0]*v for _ in range(v)]
for _ in range(e):
    u,w,c=map(int,input().split())
    g[u][w]+=c
flow=0
while True:
    parent=[-1]*v
    parent[0]=0
    q=deque([0])
    while q and parent[v-1]==-1:
        u=q.popleft()
        for w in range(v):
            if parent[w]==-1 and g[u][w]>0:
                parent[w]=u
                q.append(w)
    if parent[v-1]==-1:
        break
    f=10**18
    w=v-1
    while w!=0:
        u=parent[w]
        f=min(f,g[u][w])
        w=u
    w=v-1
    while w!=0:
        u=parent[w]
        g[u][w]-=f
        g[w][u]+=f
        w=u
    flow+=f
print(flow)
