import sys
input = sys.stdin.readline

S = list(input().strip())

standard = S[0]
flip = 0
for _ in S:
    if _ != standard:
        flip += 1
        standard = _
print((flip+1)//2)