a, b = map(int, input().split())

gcd = max(a, b)
gcd_check = min(a, b)

while(gcd_check != 0):
    temp = gcd % gcd_check
    gcd, gcd_check = gcd_check, temp

print(gcd)
print( int(a*b/gcd) )