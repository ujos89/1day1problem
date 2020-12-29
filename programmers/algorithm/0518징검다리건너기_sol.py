def cross(stones, k, friends_num):
    temp = 0

    for stone in stones:
        if(stone < friends_num):
            temp += 1
        else:
            temp = 0
        if (temp >= k):
            return False
    
    return True

def solution(stones, k):
    left = 0
    right = 200000000

    while(left < right - 1):
        mid = (left + right) // 2
        if(cross(stones, k, mid)):
            left = mid
        else:
            right = mid

    #print(left)
    
    return left

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
#[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	3	3
