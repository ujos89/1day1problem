import sys

m, n = map(int, sys.stdin.readline().split())

tomato = []
for _ in range(n):
    tomato.append(list(map(int, sys.stdin.readline().split())))

#search fresh tomato, ripe tomato position
tomato_1 = []
tomato_0 = []

for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            tomato_1.append([i,j])
        elif tomato[i][j] == 0:
            tomato_0.append([i,j])

def check_emptyqueue(queue):
    status = 0
    for q in queue:
        if q:
            status += 1
    
    if status == 0:
        return True
    else:
        return False

def tomato_bfs(i, j, q):
    global tomato
    
    #left, right, up, down
    di, dj = [0,0,-1,1], [-1,1,0,0]

    for d in range(4):
        nxt_i, nxt_j = i+di[d], j+dj[d]
        if (0 <= nxt_i < n) and (0 <= nxt_j < m) and (tomato[nxt_i][nxt_j]==0):
            q.append([nxt_i, nxt_j])
            tomato[nxt_i][nxt_j] = tomato[i][j] + 1
            
def Is_tomato_ripe():
    global tomato, tomato_0, tomato_1

    #no fresh tomato
    if not tomato_1:
        return -1
    #no ripe tomato
    elif not tomato_0:
        return 0
    
    #initalize queue
    queue = []
    for _ in tomato_1:
        queue.append([_])

    while(not check_emptyqueue(queue)):
        for q in queue:
            if q:
                # print("queue", q)
                # print("i, j: ",q[0][0], q[0][1])
                tomato_bfs(q[0][0], q[0][1], q)
                q.pop(0)

    return 1

#get answer
def get_answer(answer):
    global tomato
    
    if answer == 0:
        return 0
    if answer == -1:
        return -1

    day = 0
    for i in range(n):
        for j in range(m):
            #include fresh tomato
            if tomato[i][j] == 0:
                return -1
            day = max(day, tomato[i][j])

    return day-1

print(get_answer(Is_tomato_ripe()))


# exception_case
# 11 11
# 0 0 0 0 1 0 -1 -1 0 0 0 
# 0 -1 1 1 0 0 1 1 0 0 0 
# 0 0 0 0 -1 1 0 0 1 0 0 
# 0 0 -1 0 0 -1 -1 0 0 0 -1 
# 1 1 -1 0 0 1 0 0 0 -1 1 
# -1 0 0 0 0 0 1 0 0 1 0 
# 0 1 0 -1 0 0 0 0 1 1 1 
# 0 0 0 1 0 0 0 0 0 -1 0 
# 0 0 0 0 0 0 0 0 0 0 -1 
# -1 0 0 0 0 0 1 1 0 0 1 
# -1 0 0 0 0 -1 -1 0 0 0 -1 