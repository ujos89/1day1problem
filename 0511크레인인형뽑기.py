def solution(board, moves):
    stack = []
    point = 0
    board_t = list(map(list, zip(*board)))

    for move in moves:
        for i in range(len(board_t[move-1])):
            if(board_t[move-1][i] != 0):
                if not stack:
                    stack.append(board_t[move-1][i])
                    board_t[move-1][i] = 0
                    break
                elif (stack[-1] == board_t[move-1][i]):
                    del stack[-1]
                    point += 2
                    board_t[move-1][i] = 0
                    break
                else:
                    stack.append(board_t[move-1][i])
                    board_t[move-1][i] = 0 
                    break

    return point


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])