def toggle(n,k):
    return n^(1<<k)
n,k=map(int,input().split())
print(toggle(n,k))

