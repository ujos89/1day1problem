#tsp(traveling salesman problem)
from itertools import permutations

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]

'''
#Timeout
#Brute force (2<=N<=10)
perm = permutations(list(range(N)), N)
cost = -1
for p in perm:
    tmp_cost = 0
    flag = True
    visit_idx = 0
    while visit_idx < N:
        tmp = arr[p[visit_idx]][p[(visit_idx+1)%N]]
        if tmp:
            tmp_cost += tmp
        else:
            flag = False
            break
        visit_idx += 1

    #minimum cost
    if flag and (cost > tmp_cost or cost == -1):
        cost = tmp_cost

print(cost)
'''
