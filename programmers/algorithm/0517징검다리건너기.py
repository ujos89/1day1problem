def solution(stones, k):
    stones_len = len(stones)

    friends_num = 200000000

    for i in range(0, stones_len - k + 1):
        temp = max(stones[i:i+k])
        if(friends_num > temp):
            friends_num = temp

    print(friends_num)

    return friends_num


solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
#[2, 4, 5, 3, 2, 1, 4, 2, 5, 1]	3	3