import sys
from collections import deque

def inputdata():
    input = sys.stdin.readline
    return deque(range(1, int(input())+1))
    
def main():
    queue = inputdata()
    while queue:
        num = queue.popleft()
        if not queue:
            break
        queue.append(queue.popleft())

    print(num)

if __name__=="__main__":
    main()