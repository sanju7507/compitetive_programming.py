n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
dp=[[0]*m for _ in range(n)]
dp[0][0]=a[0][0]
for i in range(n):
    for j in range(m):
        if i==0 and j==0:
            continue
        x=[]
        if i:
            x.append(dp[i-1][j])
        if j:
            x.append(dp[i][j-1])
        if i and j:
            x.append(dp[i-1][j-1])
        dp[i][j]=a[i][j]+min(x)
print(dp[n-1][m-1])
