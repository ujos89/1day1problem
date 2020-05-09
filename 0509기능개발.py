def solution(progresses, speeds):
    duration = []
    for prog, spd in zip(progresses, speeds):
        iter = 0
        while prog + spd * iter < 100:
            iter += 1
        duration.append(iter)
    #print(duration)
    
    pre = duration[0]
    for i in range(len(duration)):
        if duration[i] < pre:
            duration[i] = pre
        pre = duration[i]
    #print(duration)

    i = 0
    answer = []
    while i < len(duration):
        cnt = duration.count(duration[i])
        answer.append(cnt)
        i += cnt
    print(answer)

    
    return answer

solution([93,30,55],[1,30,5])