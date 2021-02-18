n = int(input())

# dp_screen = [0]*(n+1)
# dp_buffer = [0]*(n+1)

# for i in range(1, n+1):
#     #get options
#     #A
#     option = [dp_screen[i-1]+1]
#     update_buffer = 0
#     #ctrlA, ctrlC, ctrlV
#     if i-3>0:
#         update_buffer = dp_screen[i-3]*2
#         option.append(update_buffer)
#     #ctrlV
#     if dp_buffer[i-1]>0 :
#         option.append(dp_buffer[i-1]+dp_screen[i-1])
#     #ctrlV, ctrlV
#     if dp_buffer[i-2]:
#         option.append(dp_buffer[i-2]*2+dp_screen[i-1])

#     #buffer update
#     if update_buffer>0 and update_buffer == max(option):
#         dp_buffer[i] = dp_screen[i-3]
#         dp_screen[i] = update_buffer
#     else:
#         dp_buffer[i] = dp_buffer[i-1]
#         dp_screen[i] = max(option)

#     print(i,option)
##fail to recognize when buffer update

dp = [0] * (n+1)

for i in range(1,n+1):
    if i-4>0:
        dp[i] = max(dp[i-1]+1, dp[i-3]*2, dp[i-4]*3, dp[i-5]*4)
    else:
        dp[i] = dp[i-1]+1

print(dp[-1])

