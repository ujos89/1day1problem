import sys

def bfs(board, start_i, start_j, end_i, end_j, board_size):
    di = [1,2,2,1,-1,-2,-2,-1]
    dj = [2,1,-1,-2,-2,-1,1,2]
    queue = [[start_i,start_j]]
    board[start_i][start_j] = 0
    while queue:
        now_i, now_j = queue.pop(0)
        if now_i == end_i and now_j == end_j:
            break

        for d in range(8):
            nxt_i, nxt_j = now_i+di[d], now_j+dj[d]
            if 0<=nxt_i<board_size and 0<=nxt_j<board_size:
                if board[nxt_i][nxt_j] == -1:
                    queue.append([nxt_i,nxt_j])
                    board[nxt_i][nxt_j] = board[now_i][now_j]+1


#input
for _ in range(int(sys.stdin.readline())):
    board_size = int(sys.stdin.readline())
    start_i, start_j = map(int, sys.stdin.readline().split())
    end_i, end_j = map(int, sys.stdin.readline().split())
    board = [[-1]*board_size for _ in range(board_size)]
    bfs(board, start_i, start_j, end_i, end_j, board_size)
    print(board[end_i][end_j])