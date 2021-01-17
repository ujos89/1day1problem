import sys

N = int(sys.stdin.readline())
answer = set([])

while N>0:
    inst = sys.stdin.readline().split()
    if inst[0] == 'all':
        answer = set(range(1,21))
    elif inst[0] == 'empty':
        answer = set([])
    else:
        num = int(inst[1])
        inst = inst[0]
        if inst == 'add':
            answer.add(num)
        elif inst == 'remove':
            if num in answer:
                answer.remove(num)
        elif inst == 'check':
            if num in answer:
                print(1)
            else:
                print(0)
        elif inst == 'toggle':
            if num in answer:
                answer.remove(num)
            else:
                answer.add(num)
    N -= 1