x,y=map(float,input().split())

if y==0:
    print("Division by zero")
else:
    sign=1
    if x<0:
        x=-x
        sign=-sign
    if y<0:
        y=-y
        sign=-sign

    low=0
    high=max(1,x)

    for _ in range(100):
        mid=(low+high)/2
        if y*mid<x:
            low=mid
        else:
            high=mid

    result=sign*(low+high)/2
    print(int(round(result)) if abs(result-round(result))<1e-9 else result)
