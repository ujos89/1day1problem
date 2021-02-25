# dp = [[0]*(n//2+2) for _ in range(n+1)]

# for _ in range(n//2+2):
#     dp[0][_] = 1
#     dp[1][_] = (1+_)

# for i in range(2,n+1):
#     for j in range(n//2+2):
#         dp[i][j] = int( (i+j) / (i-1) * dp[i-1][j] )

# # get answer
# answer = [[0,0]]
# answer.append([0,1])
# answer.append([[1,0], [0,2]])
# answer.append([[1,1], [0,3]])
# for i in range(4,n+1):
#     tmp = []
#     for ans in answer[i-2]:
#         tmp.append([ans[0]+1, ans[1]])
#     tmp.append([0,i])
#     answer.append(tmp)

# tile_num = 0
# print(dp)
# for _ in answer[n]:
#     print(_)
#     tile_num += dp[_[0]][_[1]]

# print(tile_num)

n = int(input())
#fibonacci

dp = [0]*(n+1)
if n == 1:
    print(1)
else:
    dp[1], dp[2] = 1, 2

    for _ in range(3, n+1):
        dp[_] = (dp[_-1] + dp[_-2])%15746

    print(dp[n])