import sys
from collections import deque

m, n = map(int, sys.stdin.readline().split())

tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

#search fresh tomato, ripe tomato position
queue = deque()
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i,j])

def tomato_bfs(i, j, q):
    global tomato
    #left, right, up, down
    di, dj = [0,0,-1,1], [-1,1,0,0]

    for d in range(4):
        nxt_i, nxt_j = i+di[d], j+dj[d]
        if (0 <= nxt_i < n) and (0 <= nxt_j < m) and (tomato[nxt_i][nxt_j]==0):
            q.append([nxt_i, nxt_j])
            tomato[nxt_i][nxt_j] = tomato[i][j] + 1
            
def Is_tomato_ripe(tomato):
    while queue:
        tomato_bfs(queue[0][0], queue[0][1], queue)
        queue.popleft()

    answer = 0
    for i in range(n):
        for j in range(m):
            if tomato[i][j] == 0:
                return -1
            answer = max(answer, tomato[i][j])

    return abs(answer)-1

print(Is_tomato_ripe(tomato))