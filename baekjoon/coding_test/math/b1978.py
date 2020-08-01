def IsPrime(n):
    if (n==1): return False
    for i in range(2,n):
        if(n%i == 0): return False
    return True

n = int(input())
primes = list(map(int, input().split()))
num_prime = 0

for prime in primes:
    if(IsPrime(prime)):
        num_prime += 1
print(num_prime)