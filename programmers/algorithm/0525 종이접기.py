def rev(n):
    rev = []
    for i in range(len(n)-1, -1, -1):
        if (n[i] == 0):
            rev.append(1)
        elif (n[i] == 1):
            rev.append(0)
    return rev

def solution(n):
    if(n == 1):
        return [0]
    
    return solution(n-1) + [0] + rev(solution(n-1))

for i in range(5):
    print(solution(i))

'''
1	[0]
2	[0,0,1]
3	[0,0,1,0,0,1,1]
'''