n, k = map(int, input().split())

arr = [0] * 100002
queue = [n]

def get_nxt_pos(pos):
    nxt_pos = []
    if 0<=pos-1<100002:
        nxt_pos.append(pos-1)
    if 0<=pos+1<100002:
        nxt_pos.append(pos+1)
    if 0<=pos*2<100002:
        nxt_pos.append(pos*2)

    return nxt_pos

while queue:
    pos = queue.pop(0)
    if pos == k:
        break

    for nxt_pos in get_nxt_pos(pos):
        if not arr[nxt_pos]:
            queue.append(nxt_pos)
            arr[nxt_pos] = arr[pos]+1

print(arr[k])