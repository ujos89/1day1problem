import sys

N, M = map(int, sys.stdin.readline().split())

'''
#fail: bfs?
relation = [[0 for _ in range(N)] for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relation[a][b] = 1

flag = 0
status = [0 for _ in range(N)]

print(relation)

def bfs(status, now_idx):
    global relation, flag

    if sum(status) >= 5:
        flag = 1
        return

    for i in range(N):
        if relation[now_idx][i] == 1:
            status[now_idx] = 1
            status[i] = 1
            #print(status, now_idx, i)
            bfs(status, i)
            status[now_idx] = 0
            status[i] = 0

bfs(status, 0)
print(flag)
'''
#dfs
relation = [[]for _ in range(N)]

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    relation[a].append(b)
    relation[b].append(a)

visited = [False] * N

def dfs(status, now_idx):
    global relation, visited

    if status == 4:
        print(1)
        exit()
    
    for next_idx in relation[now_idx]:
        if not visited[next_idx]:
            visited[next_idx] = True
            dfs(status+1, next_idx)
            visited[next_idx] = False

#test for all people
for _ in range(N):
    visited[_] = True
    dfs(0, _)
    visited[_] = False

print(0)
