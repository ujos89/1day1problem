import sys
import math

def inputdata():
    return sys.stdin.readline().rstrip()
    
def is_palindrome(num):
    if num == num[::-1]:
        return True
    else:
        return False

def main():
    while True:
        num = inputdata()
        if num == "0":
            break

        if is_palindrome(num):
            print("yes")
        else:
            print("no")

if __name__=="__main__":
    main()