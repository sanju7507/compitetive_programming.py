v, n = map(int, input().split())
c = list(map(int, input().split()))

dp = [999999] * (v + 1)
used = [-1] * (v + 1)
dp[0] = 0

for i in range(1, v + 1):
    for x in c:
        if x <= i and dp[i-x] + 1 < dp[i]:
            dp[i] = dp[i-x] + 1
            used[i] = x

if dp[v] == 999999:
    print(-1)
else:
    ans = []
    while v:
        ans.append(used[v])
        v -= used[v]
    print(len(ans))
