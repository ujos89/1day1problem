import sys

n = int(sys.stdin.readline())
graph = [] 
for _ in range(n):
    graph.append(list(map(int,sys.stdin.readline().strip())))

def get_pos(i,j):
    answer = []
    lrud = [[i-1,j], [i+1, j], [i, j-1], [i,j+1]]
    for pos in lrud:
        if pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < n:
            if graph[pos[0]][pos[1]] == 1:
                answer.append(pos)

    return answer

def bfs(i,j):
    global graph
    count = 0
    queue = []

    #for first depth
    graph[i][j] = 0
    count += 1
    queue.extend(get_pos(i,j))

    while(queue):
        graph[queue[0][0]][queue[0][1]] = 0
        #print("queue:",queue)
        
        for _ in get_pos(queue[0][0],queue[0][1]):
            if _ not in queue:
                queue.append(_)
        count += 1
        queue.pop(0)

    return count

def apartment():
    global graph

    apa_cnt = 0
    apa_list = []

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1:
                tmp = bfs(i,j)
                apa_cnt += 1
                apa_list.append(tmp)

    return apa_cnt, apa_list

apa_cnt, apa_list = apartment()
apa_list.sort()

print(apa_cnt)
for _ in apa_list:
    print(_)