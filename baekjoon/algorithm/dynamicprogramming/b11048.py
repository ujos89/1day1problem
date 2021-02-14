import sys
n, m = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] 

answer = [[0 for _ in range(m+1)]for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        #ignore path x,y -> x+1,y+1
        answer[i][j] = maze[i-1][j-1] + max(answer[i-1][j], answer[i][j-1])

print(answer[n][m])