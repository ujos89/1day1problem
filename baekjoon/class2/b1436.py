import sys

def inputdata():
    input = int(sys.stdin.readline())
    return input

def main():
    n = inputdata()
    num_666, title = 0, 0
    while True:
        if n ==num_666:
            break
        title += 1
        if '666' in str(title):
            num_666 += 1
        
    print(title)

if __name__=="__main__":
    main()