def gcd(a,b):
    return gcd(b%a, a) if b%a else a

n = int(input())

for m in range(n):
    temp = list(map(int, input().split()))
    gcd_temp = 0
    
    for i in range(temp[0]-1):
        for j in range(i+1,temp[0]):
            gcd_temp += gcd(temp[i+1], temp[j+1])
    print(gcd_temp)