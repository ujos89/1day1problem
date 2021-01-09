def intersection(nums1, nums2):
    answer = []
    dict1 = {_:0 for _ in nums1}
    dict2 = {_:0 for _ in nums2}
    for _ in list(dict1.keys()):
        if _ in dict2:
            answer.append(_)
    return answer

print(intersection([1,2,2,1],[2,3,2,1]))