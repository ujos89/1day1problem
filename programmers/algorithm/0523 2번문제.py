def solution(n):
    num_bin = bin(n)
    length = len(bin(n)) - 2
    num = 0

    for idx in range(1, length+1):
        num += (3 ** (idx-1)) * int(num_bin[-idx])

    return num

solution(4)



'''
4	9
11	31
'''