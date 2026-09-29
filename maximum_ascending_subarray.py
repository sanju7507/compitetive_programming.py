n=int(input())
arr=list(map(int,input().split()))
current=arr[0]
max_arr=arr[0]
for i in range(1,n):
    if arr[i]>arr[i-1]:
        current+=arr[i]
    else:
        current=i
    if current>max_arr:
        max_arr=current
    
print(max_arr)
    
    
