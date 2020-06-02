def solution(citations):
    citations.sort()
    len_cit = len(citations)

    for i in range(len_cit):
        if(citations[i] >= len_cit -i):
            return len_cit-i

    return 0

print(solution([3, 0, 6, 1, 5]))
'''
 [3, 0, 6, 1, 5]	3   
01356
'''