def solution(dirs):
    visit = []
    pos = [0, 0]

    for direction in dirs:
        if(direction == 'U'):
            if ( pos[1] < 5 ):
                pos[1] += 1
                if ((pos[0], pos[1]-1), (pos[0], pos[1])) not in visit:
                    visit.append( ((pos[0], pos[1]-1), (pos[0], pos[1])) )
                    visit.append( ((pos[0], pos[1]), (pos[0], pos[1]-1)) )
                else:
                    pass
        elif(direction == 'L'):
            if ( pos[0] > -5 ):
                pos[0] -= 1
                if ((pos[0]+1, pos[1]), (pos[0], pos[1])) not in visit:
                    visit.append( ((pos[0]+1, pos[1]), (pos[0], pos[1])) )
                    visit.append( ((pos[0], pos[1]), (pos[0]+1, pos[1])) )
                else:
                    pass
        elif(direction == 'R'):
            if ( pos[0] < 5 ):
                pos[0] += 1
                if ((pos[0]-1, pos[1]), (pos[0], pos[1])) not in visit:
                    visit.append( ((pos[0]-1, pos[1]), (pos[0], pos[1])) )
                    visit.append( ((pos[0], pos[1]), (pos[0]-1, pos[1])) )
                else:
                    pass
        elif(direction == 'D'):
            if ( pos[1] > -5 ):
                pos[1] -= 1
                if ((pos[0], pos[1]+1), (pos[0], pos[1])) not in visit:
                    visit.append( ((pos[0], pos[1]+1), (pos[0], pos[1])) )
                    visit.append( ((pos[0], pos[1]), (pos[0], pos[1]+1)) )
                else:
                    pass

    #print(visit)
    return len(visit) // 2

print(solution("LULLLLLLU"))


'''
dirs	answer
ULURRDLLU	7
LULLLLLLU	7
'''