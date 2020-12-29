
def solution(progresses, speeds):
    Q = []
    for prog, spd in zip(progresses, speeds): 
        #음수에서 몫을 구하면 올림을 해주니까 연산이 줄어든다
        if len(Q) == 0 or Q[-1][0] < -( (prog - 100) // spd ):
            Q.append([ -( (prog - 100) // spd ), 1 ])
        else:
            Q[-1][1] += 1
    #print(Q)

    return [q[1] for q in Q]

solution([93,30,55],[1,30,5])