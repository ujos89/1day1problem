from itertools import combinations
def isPrime(num):
    if(num <= 1):
        return False
    for i in range(2,num):
        if(num % i == 0):
            return False
    return True

    

def solution(nums):
    answer = 0
    comb = list(combinations(nums, 3))
    for i in range(len(comb)):
        temp_sum = comb[i][0] + comb[i][1] + comb[i][2]
        if(isPrime(temp_sum)):
            answer += 1

    #print(answer)


    return answer

solution([1,2,7,6,4])
'''
[1,2,3,4]	1
[1,2,7,6,4]	4
'''