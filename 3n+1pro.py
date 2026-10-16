i,j=map(int,input().split())
start=i
end=j
if i>j:
    i,j=j,i
max_cycle=0
for num in range(i,j+1):
    n=num
    count=1
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            n=3*n+1
        count+=1
    if count>max_cycle:
        max_cycle=count
print(start,end,max_cycle)
