import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(input()) for _ in range(n)]
coins.sort(reverse=True)

dp = [0]*100001

for c in coins:
    dp[c] = 1

for i in range(1,k+1):
    if i in coins:
        continue
    tmp = []
    for c in coins:
        if i-c>0:
            if dp[i-c]:
                tmp.append(dp[i-c])
    if tmp:
        dp[i] = min(tmp) + 1

#get answer
answer = dp[k]
if answer:
    print(answer)
else:
    print(-1)