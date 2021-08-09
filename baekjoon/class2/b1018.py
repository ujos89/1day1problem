import sys

valid_board1, valid_board2 = [[0]*8 for _ in range(8)], [[0]*8 for _ in range(8)]
for i in range(8):
    for j in range(8):
        if (i+j)%2==0:
            valid_board1[i][j] += 1
        else:
            valid_board2[i][j] += 1

def inputdata():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    board = [list(input().replace('W','0').replace('B','1'))[:-1] for _ in range(n)]
    board_int = [list(map(int, _)) for _ in board]

    return [n, m], board_int

def diff_board(board1, board2):
    diff = 0
    for i in range(8):
        for j in range(8):
            diff += abs(board1[i][j]-board2[i][j])
    
    return diff

def main():
    size, board = inputdata()
    fix = 64

    for i in range(size[0]-7):
        for j in range(size[1]-7):
            target_board = [line[j:j+8] for line in board[i:i+8]]
            # print(i, j, target_board)
            fix_temp = min(diff_board(valid_board1, target_board), diff_board(valid_board2, target_board))
            fix = min(fix_temp, fix)

    print(fix)

if __name__ == "__main__":
    main()