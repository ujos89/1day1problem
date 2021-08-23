import sys
from collections import deque

def inputdata():
    input = sys.stdin.readline
    info = []

    for _ in range(int(input())):
        n, m = map(int, input().split())
        q = list(map(int, input().split()))
        info.append([m, q])
    return info

def check_importance(importance, queue):
    for now in queue:
        now_idx, now_importance = now
        if now_importance > importance:
            return False 
    return True

def travel_queue(target, importance):
    queue = deque()
    for idx, imp in enumerate(importance):
        queue.append([idx, imp])
    
    num_out_queue = 0

    while True:
        num_out_queue += 1
        info = queue.popleft()
        num, importance = info
        if check_importance(importance, queue):
            if num == target:
                break
        else:
            queue.append([num, importance])
            num_out_queue -= 1
    
    print(num_out_queue)

def main():
    for info in inputdata():
        target, importance = info
        travel_queue(target, importance)

if __name__=="__main__":
    main()