def intersection(nums1, nums2):
    answer = []
    dict1 = {}
    for _ in nums1:
        if _ not in dict1:
            dict1[_] = 1
        else:
            dict1[_] += 1
    dict2 = {}
    for _ in nums2:
        if _ not in dict2:
            dict2[_] = 1
        else:
            dict2[_] += 1

    for _ in list(dict1.keys()):
        if _ in dict2:
            for __ in range(min(dict1[_],dict2[_])):
                answer.append(_)
    return answer

print(intersection([1,2,2,1],[2,3,2,1]))