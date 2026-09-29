dividend,divisor=map(int,input().split())
q=int(dividend/divisor)
maxi=+214783647
mini=-214783647

if q>maxi:
    print(maxi)
elif q<mini:
    print(mini)
else:
    print(q)
