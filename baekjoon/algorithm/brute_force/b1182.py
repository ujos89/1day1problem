from itertools import combinations

N, S = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

for num in range(1,N+1):
    for subset in list(combinations(arr, num)):
        if sum(subset) == S:
            cnt += 1

print(cnt)