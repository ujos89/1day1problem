import sys
import math

def inputdata():
    input = sys.stdin.readline
    num = int(input())
    return list(map(int, input().split()))
    
def Is_prime(num):
    if num==1:
        return False
    if num==2:
        return True
    
    for n in range(2, int(math.sqrt(num))+1):
        if num%n == 0:
            return False
    return True

def main():
    primes = inputdata()
    num_prime = 0
    for prime in primes:
        if Is_prime(prime):
            num_prime += 1
    print(num_prime)

if __name__=="__main__":
    main()