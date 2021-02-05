import sys
sys.setrecursionlimit(10000)

def find_land(i, j):
    #dfs
    if graph[i][j] == 1:
        graph[i][j] = 0

        #left
        if j>0 and graph[i][j-1] == 1:
            find_land(i, j-1)
        #right
        if j<w-1 and graph[i][j+1] == 1:
            find_land(i, j+1)
        #up
        if i>0 and graph[i-1][j] == 1:
            find_land(i-1, j)
        #down
        if i<h-1 and graph[i+1][j] == 1:
            find_land(i+1, j)
        #leftup
        if j>0 and i>0 and graph[i-1][j-1] == 1:
            find_land(i-1,j-1)
        #rightup
        if j<w-1 and i>0 and graph[i-1][j+1] == 1:
            find_land(i-1,j+1)
        #leftdown
        if j>0 and i<h-1 and graph[i+1][j-1] == 1:
            find_land(i+1,j-1)
        #rightdown
        if j<w-1 and i<h-1 and graph[i+1][j+1] == 1:
            find_land(i+1,j+1)
        
        ##modify -> use dx,dy to compress code
    else:
        return

while True:
    w, h = map(int, sys.stdin.readline().split())
    if w==0 and h==0:
        break
    
    #input graph
    graph = []
    for _ in range(h):
        graph.append(list(map(int, sys.stdin.readline().split())))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1:
                cnt += 1
                find_land(i, j)

    print(cnt)

#to prevent runtime error(recursion limit) -> use bfs 