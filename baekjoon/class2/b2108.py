import sys
from collections import Counter

def inputdata():
    input = sys.stdin.readline
    len_nums = int(input())
    nums = []
    for _ in range(len_nums):
        nums.append(int(input()))
    return len_nums, nums

def mean(nums, len_nums):
    return round(sum(nums)/len_nums)

def median(nums, len_nums):
    idx = int(len_nums/2)
    return nums[idx]


def mode(nums, len_nums):
    if len_nums == 1:
        return nums[0]
    targets = Counter(nums).most_common()
    if targets[0][1] == targets[1][1]:
        return targets[1][0]
    else:
        return targets[0][0]

def range_(nums):
    return nums[-1]-nums[0]

def main():
    len_nums, nums = inputdata()
    nums = sorted(nums)
    print(mean(nums, len_nums))
    print(median(nums, len_nums))
    print(mode(nums, len_nums))
    print(range_(nums))

if __name__=="__main__":
    main()

# # timeout
# def mode(nums):
#     targets = list(set(nums))
#     counts = []
#     modes = []
#     for target in targets:
#         counts.append(nums.count(target))
    
#     min_counts = min(counts)
#     idx_mode = counts.index(min_counts)
#     modes.append(targets[idx_mode])
#     del counts[idx_mode]
#     del targets[idx_mode]

#     while counts:
#         if min_counts != min(counts):
#             break
#         idx_mode = counts.index(min(counts))
#         modes.append(targets[idx_mode])
#         del counts[idx_mode]
#         del targets[idx_mode]

#     if len(modes)==1:
#         return modes[0]
#     else:
#         return sorted(modes)[1]