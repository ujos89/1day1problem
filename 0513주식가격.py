def solution(prices):
    answer = []

    for i in range(len(prices)):
        j = i
        while (prices[j] >= prices[i] and j < len(prices)-1 ):
            j += 1
        answer.append(j-i)
    #print(answer)
    return answer

solution([1,2,3,2,3])