n=int(input())
a=list(map(float,input().split()))
mn=min(a)
mx=max(a)
buckets=[[] for _ in range(n)]
for x in a:
    if mx==mn:
        index=0
    else:
        index=int((x-mn)/(mx-mn)*(n-1))
    buckets[index].append(x)
for bucket in buckets:
    bucket.sort()
result=[]
for bucket in buckets:
    result.extend(bucket)
print(" ".join(f"{x:.2f}" if x%1!=0 else f"{int(x)}" for x in result))
