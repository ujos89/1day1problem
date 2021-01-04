N = int(input())

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

for _ in permuation(N):
    print(*_)