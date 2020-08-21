#날짜계산

calender = []
for i in range(15*28*19):
  calender.append([i % 15 + 1, i % 28 + 1, i % 19 + 1])
x = list(map(int,input().split()))
print(calender.index(x) + 1)