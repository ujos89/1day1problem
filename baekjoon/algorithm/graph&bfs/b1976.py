import sys

city_num = int(sys.stdin.readline())
travel_city_num = int(sys.stdin.readline())
city_map = [list(map(int, sys.stdin.readline().split())) for _ in range(city_num)]
travel_plan = list(map(int, sys.stdin.readline().split()))

visited = [False] * city_num
disjoint_city = [-1] * city_num
disjoint_check = 0

def bfs(queue, disjoint_check):
    while(queue):
        now_city = queue.pop(0)
        visited[now_city] = True
        disjoint_city[now_city] = disjoint_check

        for nxt_city in range(city_num):
            if city_map[now_city][nxt_city] and not visited[nxt_city]:
                queue.append(nxt_city)

queue = []
for idx in range(city_num):
    if not visited[idx]:
        queue.append(idx)
        bfs(queue, disjoint_check)
        disjoint_check += 1

def Is_travel(disjoint_city):
    check = disjoint_city[travel_plan[0]-1]
    for city in travel_plan:
        if disjoint_city[city-1] != check:
            return print("NO")
    return print("YES")
    
Is_travel(disjoint_city)
