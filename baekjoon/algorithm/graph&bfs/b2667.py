import sys

n = int(sys.stdin.readline())

graph = [] 
for _ in range(n):
    graph.append(list(sys.stdin.readline().strip()))

print(graph)