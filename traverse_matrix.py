n,m=map(int,input().split())
a=[list(map(int,input().split())) for _ in range(n)]
top,left=0,0
bottom,right=n-1,m-1
ans=[]
while top<=bottom and left<=right:
    for j in range(left,right+1):
        ans.append(a[top][j])
    top+=1
    for i in range(top,bottom+1):
        ans.append(a[i][right])
    right-=1
    if top<=bottom:
        for j in range(right,left-1,-1):
            ans.append(a[bottom][j])
        bottom-=1
    if left<=right:
        for i in range(bottom,top-1,-1):
            ans.append(a[i][left])
        left+=1
print(*ans)
