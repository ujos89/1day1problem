def solution(info, query):
    people = []
    for info_ in info:
        tmp = info_.split()
        score = int(tmp.pop())
        tmp = set(tmp)
        people.append([tmp, score])
    

    conditions = []
    for query_ in query:
        tmp = query_.replace('-', '')
        tmp = tmp.replace(' and ', ' ').split()
        score = int(tmp.pop())
        tmp = set(tmp)
        conditions.append([tmp, score])

    answer = []
    for condition in conditions:
        count = 0
        for person in people:
            if (not condition[0] - person[0]) and condition[1] <= person[1]:
                count +=1
        answer.append(count)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))

# result: [1,1,1,1,2,4] 