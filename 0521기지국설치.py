import math
def solution(n, stations, w):
    apart = []
    for i in range(1, len(stations)):
        apart.append((stations[i]-w-1) - (stations[i-1]+w))

    apart.append(stations[0]-w-1)
    apart.append(n - (stations[-1]+w))
    
    answer = 0
    for i in apart:
        if i <= 0: continue
        answer += math.ceil(i/((w*2)+1))

    print(answer)
    return answer

solution(11,[4,11],1)
solution(16,[9],2)

'''
N	stations	W	answer
11	[4, 11]	1	3
16	[9]	2	3
'''