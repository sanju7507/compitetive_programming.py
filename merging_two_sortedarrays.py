n1=int(input())
arr1=list(map(int,input().split()))
n2=int(input())
arr2=list(map(int,input().split()))
merged=arr1+arr2
print(*sorted(merged))
