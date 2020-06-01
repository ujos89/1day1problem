def solution(people, limit):
    safe_num = 0
    people.sort()
    left_idx = 0
    right_idx = len(people) - 1

    while (left_idx <= right_idx):
        if(people[left_idx]+people[right_idx] <= limit):
            left_idx += 1
        right_idx -= 1
        safe_num += 1

    return safe_num

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))


'''
people	limit	return
[70, 50, 80, 50]	100	3
[70, 80, 50]	100	3
'''