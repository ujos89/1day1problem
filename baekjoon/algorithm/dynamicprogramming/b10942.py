import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
iters = int(sys.stdin.readline())

def Is_palindrome(nums):
    for idx in range(len(nums)//2):
        if nums[idx] != nums[-1-idx]:
            return 0
    return 1

# #start, end, length
# longest = [len(nums), 0, -1]
# for _ in range(iters):
#     s, e = map(int, sys.stdin.readline().split())
#     start, end = s-1, e
#     if longest[0] < start and longest[1] > end and start-longest[0] == longest[1]-end:
#         print(1)
#     else:
#         print(Is_palindrome(nums[start:end]))

#     print(nums[s-1:e])
#     print(Is_palindrome(nums[s-1:e]))

dp = [[0]*n for _ in range(n)]

#length of palindrome = 1
for _ in range(n):
    dp[_][_] = 1

#length of palindrome = 2
for _ in range(n-1):
    if nums[_]==nums[_+1]:
        dp[_][_+1] = 1

#length of palindrome > 2
for _ in range(2,n):
    for s in range(n-_):
        if nums[s]==nums[s+_] and dp[s+1][s+_-1] == 1:
            dp[s][s+_] = 1

#test for m
for _ in range(iters):
    s, e =map(int, sys.stdin.readline().split())
    print(dp[s-1][e-1]) 