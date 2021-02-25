import sys
from itertools import combinations, permutations

n = int(sys.stdin.readline().strip())
ability = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

ability_gap = 100*2*10*9
for comb in combinations(range(n), n//2):
    team_a = list(comb)
    team_b = []
    for _ in range(n):
        if _ not in team_a:
            team_b.append(_)
    
    #calculate ability
    ability_a, ability_b = 0, 0
    for per in permutations(team_a, 2):
        ability_a += ability[per[0]][per[1]]
    for per in permutations(team_b, 2):
        ability_b += ability[per[0]][per[1]]

    ability_gap = min(abs(ability_a-ability_b), ability_gap)

print(ability_gap)


