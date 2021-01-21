import sys

#python have limitation for recursion
sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

def dfs(idx):
    global graph, visited

    if(all(visited)):
        return

    visited[idx] = True

    for nxt_idx in graph[idx]:
        if not visited[nxt_idx]:
            dfs(nxt_idx)

#main
dfs(0)
cnt = 1
while not all(visited):
    cnt += 1
    dfs(visited.index(False))

print(cnt)
