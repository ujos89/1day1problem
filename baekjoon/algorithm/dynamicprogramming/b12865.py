import sys

#0-1 knapsack problem
n, max_weight = map(int, sys.stdin.readline().split())
objects = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

#1st try:dynamic programming
# dp = [0]*(max_weight+1)
# for obj in objects:
#     dp[obj[0]] = obj[1]

# for w in range(1,max_weight+1):
#     for i in range(w-1,0,-1):
#         for j in range(min(w-i,i),0,-1):
#             dp[w] = max(dp[w], dp[i]+dp[j])

# print(dp[-1])
# #time over

#2nd try
dp = [[0]*(max_weight+1) for _ in range(n+1)]
for obj_idx in range(1, n+1):
    for bag_weight in range(1, max_weight+1):
        obj_weight = objects[obj_idx-1][0]
        obj_value = objects[obj_idx-1][1]

        #impossible to pack i-th object
        if obj_weight > bag_weight:
            dp[obj_idx][bag_weight] = dp[obj_idx-1][bag_weight]
        else:
            dp[obj_idx][bag_weight] = max(dp[obj_idx-1][bag_weight-obj_weight] + obj_value, dp[obj_idx-1][bag_weight])

print(dp[-1][-1])