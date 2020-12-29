import re
 
def solution(s):
    answer = []
    a = s.split(',{')
    a.sort(key = len)

    for i in a:
        num = re.findall("\d+", i)
        for k in num:
            if int(k) not in answer:
                answer.append(int(k))
    
    #print(answer)
    return answer

solution("{{4,2,3},{3},{2,3,4,14},{2,3}}")