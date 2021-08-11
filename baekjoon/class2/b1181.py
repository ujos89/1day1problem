import sys
from collections import OrderedDict

def inputdata():
    input = sys.stdin.readline
    words_num = int(input())
    words = {}
    for _ in range(words_num):
        word = input().rstrip('\n')
        key = len(word)
        if key not in words:
            words[key] = [word]
        elif key in words:
            if word not in words[key]:
                words[key].append(word)

    return words

def printwords(words):
    words = OrderedDict(sorted(words.items()))
    for word_arr in words.values():
        for word in sorted(word_arr):
            print(word)

def main():
    words = inputdata()
    printwords(words)

if __name__=="__main__":
    main()