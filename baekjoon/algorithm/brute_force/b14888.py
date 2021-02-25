import sys
from itertools import permutations

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
# +, -, *, /
operator = list(map(int, sys.stdin.readline().split()))
oper = []
for idx, iters in enumerate(operator):
    for _ in range(iters):
        oper.append(idx)

def cal(nums, oper):
    result = nums[0]
    for idx in range(1, n):
        if oper[idx-1] == 0:
            result += nums[idx]
        elif oper[idx-1] == 1:
            result -= nums[idx]
        elif oper[idx-1] == 2:
            result *= nums[idx]
        elif oper[idx-1] == 3:
            if result < 0:
                result = -((-result)//nums[idx])
            else:
                result = result // nums[idx]
    return result

min_val = max_val = cal(nums, oper)

for op in set(permutations(oper, n-1)):
    tmp = cal(nums, op)
    min_val = min(tmp, min_val)
    max_val = max(tmp, max_val)

print(max_val)
print(min_val)