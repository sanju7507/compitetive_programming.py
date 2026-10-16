a,b=map(int,input().split())
def egcd(a,b):
    if b==0:
        return a,1,0
    g,x1,y1=egcd(b,a%b)
    return g,y1,x1-(a//b)*y1
g,x,y=egcd(a,b)
k1=(-x)//(b//g)
k2=k1+1
best=None
for k in range(k1-2,k2+3):
    xx=x+k*(b//g)
    yy=y-k*(a//g)
    cur=(abs(xx)+abs(yy),xx>yy,xx,yy)
    if best is None or cur<best:
        best=cur
print(best[2],best[3],g)


