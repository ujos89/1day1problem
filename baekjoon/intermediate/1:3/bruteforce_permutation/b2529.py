import sys
from itertools import permutations

def inputdata():
    input = sys.stdin.readline
    inequality_num = int(input())
    inequality = list(input().strip().split())
    return inequality_num, inequality

def inequ_test(inequ, p):
    for idx in range(len(inequ)):
        a, b = p[idx], p[idx+1] 
        if inequ[idx] == '<' and a>b:
            return False
        elif inequ[idx] == '>' and a<b:
            return False
    return True

def get_min(inequ, num):
    perm = permutations(range(10), num+1)
    
    for p in perm:
        if inequ_test(inequ, p):
            return p
    return 0

def get_max(inequ, num):
    perm = reversed(list(permutations(range(10), num+1)))

    for p in perm:
        if inequ_test(inequ, p):
            return p
    return 0

def main():
    inequ_num, inequ = inputdata()
    
    min_p = get_min(inequ, inequ_num)
    max_p = get_max(inequ, inequ_num)
    
    for _ in max_p:
        print(_, end='')
    print()
    for _ in min_p:
        print(_, end='')
    print()

if __name__=="__main__":
    main()
