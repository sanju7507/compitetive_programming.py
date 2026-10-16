s=input().strip()
seen=0
dup=0
ans=[]
for c in s:
    bit=1<<(ord(c)-97)
    if seen&bit:
        dup|=bit
    else:
        seen|=bit
for c in s:
    bit=1<<(ord(c)-97)
    if dup&bit:
        ans.append(c)
        dup^=bit
print(" ".join(ans) if ans else "No duplicates")
