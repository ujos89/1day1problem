from itertools import combinations

comb_list = []
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    else:
        comb_list.append(arr[1:])

for c in comb_list:
    for _ in list(combinations(c, 6)):
        print(*_)
    print()