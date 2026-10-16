n=int(input())
a=list(map(int,input().split()))
total=sum(a)
k=n//2
ans=total
def solve(i,cnt,s):
    global ans
    if cnt==k:
        ans=min(ans,abs(total-2*s))
        return
    if i==n or n-i<k-cnt:
        return
    solve(i+1,cnt+1,s+a[i])
    solve(i+1,cnt,s)
solve(0,0,0)
print(ans)
