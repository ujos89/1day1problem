N = int(input())
arr = list(map(int, input().split()))

def permuation(N):
    if N == 1:
        return [[1]]
    else:
        answer = []
        for iter in range(N):
            for tmp in permuation(N-1):
                tmp.insert(iter, N)
                answer.append(tmp)
        answer.sort()
        return answer

def get_diff(arr):
    diff = 0
    for idx in range(0, len(arr)-1):
        diff += abs(arr[idx] - arr[idx+1])
    return diff

def shuffle_arr(N, arr):
    shuffle = permuation(N)
    max_val = get_diff(arr)
    for s in shuffle:
        arr_shuffled = [0 for _ in range(N)]
        for idx in range(len(arr)):
            arr_shuffled[s[idx]-1] = arr[idx]
        #print(s, arr_shuffled)
        tmp = get_diff(arr_shuffled)
        if tmp > max_val:
            max_val = tmp

    return max_val

print(shuffle_arr(N, arr))