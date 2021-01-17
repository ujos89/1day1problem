N = int(input())
T, P = [0 for _ in range(N)], [0 for _ in range(N)]
answer = [0 for _ in range(N+1)]
for i in range(N):
    T[i], P[i] = map(int, input().split())

#Dynamic programming
for idx in range(N-1, -1, -1):
    if T[idx] + idx > N:
        answer[idx] = answer[idx+1]
    else:
        answer[idx] = max(P[idx]+answer[idx+T[idx]], answer[idx+1])

print(answer[0])