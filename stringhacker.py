a=input().strip()
n=len(a)
b=a[::-1]
pre=[0]*(n+1)

for i in range(1,n+1):
    current=[0]*(n+1)
    for j in range(1,n+1):
        if a[i-1]==b[j-1]:
            current[j] = 1 + pre[j-1]
        else:
            current[j]=max(pre[j],current[j-1])
    pre=current
print(pre[n])
        

    
