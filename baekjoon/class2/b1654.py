import sys
sys.setrecursionlimit(1000000)

def inputdata():
    input = sys.stdin.readline
    lan_have, lan_need = map(int, input().split()) 
    lans = [int(input()) for _ in range(lan_have)]
    return lans, lan_need

def binarysearch(left, right, lans, lan_need):
    if left > right:
        return right
    mid = (left+right)//2

    lan_made = 0
    for lan in lans:
        lan_made += lan//mid

    # if lan_need == lan_made:
    #     print("return: ",left, right, mid)
    #     return mid
    # print(left, right, mid, lan_made)    

    if lan_made >= lan_need:
        return binarysearch(mid+1, right, lans, lan_need)
    else:
        return binarysearch(left, mid-1, lans, lan_need)

def main():
    lans, lan_need = inputdata()
    lan = binarysearch(0, 2**31-1, lans, lan_need)
    print(lan)


if __name__=="__main__":
    main()