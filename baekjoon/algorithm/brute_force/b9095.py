def plus123(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return plus123(num-1)+plus123(num-2)+plus123(num-3)

case = int(input())
for _ in range(case):
    num = int(input())
    print(plus123(num))