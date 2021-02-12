import sys

n = int(sys.stdin.readline())

# answer = 0
# while(n!=1):
#     if n%3 == 0:
#         n /= 3
#         answer += 1
#     elif n%2 == 0:
#         n /= 2
#         answer += 1
#     else:
#         n -= 1
#         answer += 1

#     print(answer, n)
# exception: 10->5->4->2->1, 10->9->3->1

answer = [0, 0]
for i in range(2, n+1):
    tmp = [answer[-1]+1]
    if not i%2:
        tmp.append(answer[i//2]+1)
    if not i%3:
        tmp.append(answer[i//3]+1)
    answer.append(min(tmp))

print(answer[-1])