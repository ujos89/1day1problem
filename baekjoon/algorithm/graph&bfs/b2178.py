import sys

n, m = map(int, sys.stdin.readline().split())

maze = []
for _ in range(n):
    maze.append(list(sys.stdin.readline()))

#bfs
queue = [[0,0]]
maze[0][0] = 1
#left, right, up, down
di, dj = [0,0,-1,1], [-1,1,0,0]

while(queue):
    i, j = queue[0][0], queue[0][1]    
    queue.pop(0)

    for direction in range(4):
        nxt_i, nxt_j = di[direction]+i, dj[direction]+j
        if (0 <= nxt_i < n) and (0 <= nxt_j < m) and (maze[nxt_i][nxt_j]=='1'):
            queue.append([nxt_i,nxt_j])
            maze[nxt_i][nxt_j] = maze[i][j] + 1

print(maze[n-1][m-1])