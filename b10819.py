N = int(input())
arr = list(map(int, input().split()))

def get_diff(arr):
    diff = 0
    for idx in range(0, len(arr)-1):
        diff += abs(arr[idx] - arr[idx+1])
    return diff

def suffle_arr(arr):
    


print(get_diff(arr))