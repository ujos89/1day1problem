import sys
n = int(sys.stdin.readline())
array = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]

def bfs(i, j):
    queue = []
    queue.append([i,j])
    move = [[0,1],[1,0]]

    while queue:
        x, y = queue[0][0], queue[0][1]
        tmp = array[x][y]
        queue.pop(0)
        
        for mv in move:
            nxt_x, nxt_y = x+mv[0]*tmp, y+mv[1]*tmp
            if x==3 and y==3:
                pass
            elif 0<=nxt_x<n and 0<=nxt_y<n:
                dp[nxt_x][nxt_y] += 1
                queue.append([nxt_x, nxt_y])

def dynamic():
    for i in range(n):
        for j in range(n):
            if i==n-1 and j==n-1:
                break
            tmp = array[i][j]
            d, r = i+tmp, j+tmp

            if 0<=d<n:
                dp[d][j] += dp[i][j]
            if 0<=r<n:
                dp[i][r] += dp[i][j]


dp[0][0]=1
dynamic()
print(dp[n-1][n-1])