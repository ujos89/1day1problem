def prime_list(n):
    sieve = [True] * n
    sieve[0] = False
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if (sieve[i] == True):
            for j in range(i+i, n, i):
                sieve[j] = False
    
    return [[i for i in range(3,n) if sieve[i] == True], sieve]

def goldbach(n, primes):
    if (n==0): return
    for prime in primes[0]:
        if (primes[1][n-prime]):
            print(n,"=",prime,"+",n-prime)
            return
    print("Goldbach's conjecture is wrong.") 

n = -1
primes = prime_list(1000000)
while(n != 0):
    n = int(input())
    goldbach(n, primes)