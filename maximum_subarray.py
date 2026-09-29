n=int(input())
arr=list(map(int,input().split()))
current=arr[0]
maxi=arr[0]
for i in range(1,n):
    current=max(arr[i],current+arr[i])
    maxi=max(maxi,current)
print(maxi)
