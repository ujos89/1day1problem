import sys
from collections import deque

def inputdata():
    input = sys.stdin.readline
    node_num = int(input())
    graph = [[] for _ in range(node_num)]
    for _ in range(int(input())):
        i, j = map(int, input().split())
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    return node_num, graph

def bfs(start, node_num, graph):
    queue = deque([start])
    visited = [False] * node_num

    while queue:
        now_pos = queue.popleft()
        visited[now_pos] = True
        for nxt_pos in graph[now_pos]:
            if not visited[nxt_pos]:
                queue.append(nxt_pos)
    
    #print(visited)
    return sum(visited)

def main():
    node_num, graph = inputdata()
    answer = bfs(0, node_num, graph)
    print(answer-1)

if __name__ == "__main__":
    main()