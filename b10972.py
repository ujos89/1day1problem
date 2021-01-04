N = int(input())
arr = list(map(int, input().split()))

if arr == list(reversed(range(1,N+1))):
    print(-1)
else:
    before_num = 0
    for idx, num in enumerate(reversed(arr)):
        if before_num:
            if before_num > num:
                pos = N - idx - 1
                break
        before_num = num

    tmp = arr.copy()
    tmp1 = tmp[pos:]
    tmp1.sort()
    #print(pos)
    #print(tmp1)
    answer = arr[:pos]
    answer.append(tmp1[tmp1.index(arr[pos])+1])
    for _ in answer:
        if _ in tmp:
            tmp.remove(_)
    tmp.sort()
    answer.extend(tmp)
    print(*answer)