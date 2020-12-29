def solution(heights):
    l = len(heights)
    answer = [0 for i in range(l)]
    
    while heights:
        temp = heights.pop()
        for idx in range(len(heights)-1, -1, -1):
            if(heights[idx] > temp):
                answer[len(heights)] = idx + 1
                break

    #print(answer)
    return answer

solution([3,9,9,3,5,7,2])
solution([6,9,5,7,4])
solution([1,5,3,6,7,6,5])