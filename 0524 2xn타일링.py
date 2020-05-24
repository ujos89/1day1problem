def solution(n):
    if(n <= 2):
        return n
    
    temp = [ ]
    temp.append(1)
    temp.append(2)

    for i in range(2, n):
        temp.append((temp[i-1] + temp[i-2])%1000000007)
    
    return temp[-1]
    
for i in range(1,10):
    print(solution(i))


'''
n = 1, 1 
n = 2, 2
n = 3, 3
n = 4, 5
'''