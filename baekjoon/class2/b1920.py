import sys

def inputdata():
    input = sys.stdin.readline
    n = int(input())
    arr_n = set(map(int, input().rstrip().split()))
    m = int(input())
    arr_m = list(map(int, input().rstrip().split()))

    return arr_n, arr_m
    
def main():
    arr_n, arr_m = inputdata()
    for m in arr_m:
        if m in arr_n:
            print(1)
        else:
            print(0)

if __name__=="__main__":
    main()