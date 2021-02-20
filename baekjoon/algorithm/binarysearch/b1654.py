import sys
from itertools import combinations

n, needs = map(int, sys.stdin.readline().split())
lans = [int(input()) for _ in range(n)]

def get_lan_num(lans, standard):
    lan_num = 0
    for lan in lans:
        lan_num += lan//standard
    return lan_num

def binarysearch(left, right):
    global lans, needs
    
    if left >= right-1:
        print((left+right)//2)
        return
    
    mid = (left+right)//2
    #print(left,mid,right)
    if get_lan_num(lans, mid) >= needs:
        binarysearch(mid, right)
    else:
        binarysearch(left, mid)

binarysearch(1,max(lans)+1)