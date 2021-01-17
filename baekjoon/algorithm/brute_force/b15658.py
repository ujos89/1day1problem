from itertools import permutations

#input
N = int(input())
num = list(map(int, input().split()))
oper_num = list(map(int, input().split()))

min_answer = 1000000001
max_answer = -1000000001
'''
#brute force -> time-out
#1:+, 2:-, 3:*, 4://
oper = []
for i, _ in enumerate(oper_num):
    tmp = [i+1]*_
    oper.extend(tmp)

for per in permutations(oper, N-1):
    answer = num[0]
    for idx in range(N-1):
        if per[idx] == 1:
            answer += num[idx+1]
        elif per[idx] == 2:
            answer -= num[idx+1]
        elif per[idx] == 3:
            answer *= num[idx+1]
        elif per[idx] == 4:
            if answer > 0 :
                answer = answer//num[idx+1]
            else:
                answer = -(-answer//num[idx+1])
        
    min_answer = min(min_answer, answer)
    max_answer = max(max_answer, answer)

print(max_answer)
print(min_answer)
'''
#dfs
def dfs(idx, ans):
    global min_answer, max_answer, N, num, oper_num

    if idx == N-1:
        min_answer = min(ans, min_answer)
        max_answer = max(ans, max_answer)
        return

    for i in range(4):
        if oper_num[i] != 0:
            if i == 0:
                next_ans = ans + num[idx+1]
            elif i == 1:
                next_ans = ans - num[idx+1]
            elif i == 2:
                next_ans = ans * num[idx+1]
            else:
                if ans < 0:
                    next_ans = -(-ans//num[idx+1]) 
                else:
                    next_ans = ans // num[idx+1]

            oper_num[i] -= 1
            #print(idx, ans, num[idx+1], next_ans)
            dfs(idx+1, next_ans)
            oper_num[i] += 1

dfs(0, num[0])
print(max_answer)
print(min_answer)