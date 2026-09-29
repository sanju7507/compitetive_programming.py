def array():   
    n=int(input())
    arr=list(map(int,input().split()))
    max_val=max(arr)
    min_val=min(arr)
    max_in=arr.index(max_val)
    min_in=arr.index(min_val)
    arr[max_in],arr[min_in]=arr[min_in],arr[max_in]
    print(*(arr))
array()
