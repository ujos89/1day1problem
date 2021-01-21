import sys

n, m, v = map(int, sys.stdin.readline().split())
'''
graph = [[]for _ in range(n)]
visited = [True] * n
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if b-1 not in graph[a-1]:
        graph[a-1].append(b-1)
    if a-1 not in graph[b-1]:
        graph[b-1].append(a-1)
    visited[a-1] = False
    visited[b-1] = False

for _ in graph:
    _.sort()

dfs_list = []
def dfs(now_idx):
    global graph, dfs_list, visited_dfs

    for nxt_idx in graph[now_idx]:
        if not visited_dfs[nxt_idx]:
            dfs_list.append(nxt_idx+1)
            visited_dfs[nxt_idx] = True
            dfs(nxt_idx)

bfs_list = []
def bfs(now_idx):
    global graph, bfs_list, visited_bfs

    visited_bfs[now_idx] = True
    bfs_list.append(now_idx+1)  

    for nxt_idx in graph[now_idx]:
        if not visited_bfs[nxt_idx]:
            bfs_list.append(nxt_idx+1)
            visited_bfs[nxt_idx]= True

    if False not in visited_bfs:
        return
    else:
        bfs(visited_bfs.index(False))

#dfs
visited_dfs = visited.copy()
visited_dfs[v-1] = True
dfs_list.append(v)
dfs(v-1)
print(*dfs_list)

#bfs
visited_bfs = visited.copy()
bfs(v-1)
print(*bfs_list)
pass test case but fail
'''

graph = [[0 for _ in range(n)] for _ in range(n)]
visited = [False] * n
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

#dfs
search_dfs = []
def dfs(v):
    global visited, graph, search_dfs

    if(all(visited)):
        return
    
    visited[v] = True
    search_dfs.append(v+1)

    for nxt_idx in range(n):
        if (not visited[nxt_idx] and graph[v][nxt_idx]):
            dfs(nxt_idx)

dfs(v-1)
print(*search_dfs)

#bfs
search_bfs=[]
visited = [False] * n
def bfs(v):
    global visited, graph, search_bfs

    queue = [v]
    while(queue):
        #print(queue)
        visited[queue[0]] = True
        search_bfs.append(queue[0]+1)
        
        for nxt_idx in range(n):
            if not visited[nxt_idx] and graph[queue[0]][nxt_idx]:
                queue.append(nxt_idx)
                visited[nxt_idx] = True
        
        queue.pop(0)

bfs(v-1)
print(*search_bfs)