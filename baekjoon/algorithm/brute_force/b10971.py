#tsp(traveling salesman problem)
from itertools import permutations

N = int(input())
arr = [ list(map(int, input().split())) for _ in range(N) ]
perm = permutations(list(range(N)), N)

#Brute force (2<=N<=10)
cost = -1
for p in perm:
    tmp_cost = 0
    flag = True
    for visit_idx in range(N-1):
        start = int(p[visit_idx])
        end = int(p[visit_idx+1])
        if arr[start][end]:
            tmp_cost += arr[start][end]
        else:
            flag = False
    
    #final country to first country
    if arr[int(p[-1])][int(p[0])]:
        tmp_cost += arr[int(p[-1])][int(p[0])]
    else:  
        flag = False

    #minimum cost
    if flag and (cost > tmp_cost or cost == -1):
        cost = tmp_cost

print(cost)
