def majority(arr,n):
    for i in arr:
        if arr.count(i)>n//2:
            return i
        else:
            return -1
n=int(input())
arr=list(map(int,input().split()))
print(majority(arr,n))
