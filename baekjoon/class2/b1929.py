import sys
import math

def inputdata():
    input = sys.stdin.readline
    return map(int, input().split())
    
def Is_prime(n):
    if n == 1:
        return False
    
    end = int(math.sqrt(n))+1
    for _ in range(2, end):
        if n % _ == 0:
            return False
    return True

def main():
    n, m = inputdata()
    for num in range(n, m+1):
        if Is_prime(num):
            print(num)

if __name__=="__main__":
    main()