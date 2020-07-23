def lcm(a,b):  
    gcd = max(a,b)
    gcd_check = min(a,b)
    while(gcd_check != 0):
        temp = gcd % gcd_check
        gcd, gcd_check = gcd_check, temp
    return int(a*b/gcd)

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a,b))