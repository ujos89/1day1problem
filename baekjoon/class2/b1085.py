import sys

def inputdata():
    input = sys.stdin.readline
    return map(int, input().split())

def main():
    x, y, w, h = inputdata()
    print(min(w-x, x, h-y, y))

if __name__=="__main__":
    main()