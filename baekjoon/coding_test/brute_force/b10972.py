def permuation(num):
    return 0

N = int(input())
arr = list(map(int, input().split()))

if arr == list(reversed(range(1,N+1))):
    print(-1)
else:
    for index, value in enumerate(arr):
        print(index, value)