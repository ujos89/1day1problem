import sys
from collections import deque

def inputdata():
    input = sys.stdin.readline
    return int(input())

def stack_test(n):
    stack = deque([])
    status = 0
    log = []

    for _ in range(n):
        goal = inputdata()

        while status < goal:
            status += 1
            stack.append(status)
            log.append('+')

        if stack.pop() != goal:
            return False
        else:
            log.append('-')

    return log

def main():
    n = inputdata()
    log = stack_test(n)

    if not log:
        print("NO")
    else:
        for _ in log:
            print(_)

if __name__=="__main__":
    main()