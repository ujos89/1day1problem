import sys

city_num = int(input())
distance = list(map(int, sys.stdin.readline().split()))
gas_price = list(map(int, sys.stdin.readline().split()))

#1st try
# min_price = [0]*(city_num-1)
# for i in range(city_num-2,-1,-1):
#     min_price[i] = distance[i]*gas_price[i]

#     for j in range(i,city_num-1):
#         min_price[j] = min(distance[j] * gas_price[i], min_price[j])   
  
# print(sum(min_price))
# #time-over

#2nd try
# sum_distance = 0
# sum_gas_price = 0
# min_gas_price = 1000000000
# for i in range(city_num-2,-1,-1):
#     sum_distance += distance[i]
#     #i-th country's gas price is the lowest
#     if min_gas_price > gas_price[i]:
#         min_gas_price = gas_price[i]
#         sum_gas_price = min_gas_price * sum_distance
#     else:
#         sum_gas_price += gas_price[i] * distance[i]

#     print(sum_distance, min_gas_price, sum_gas_price)
# print(sum_gas_price)
# counter example
# 5
# 3 2 1 4
# 5 8 9 4 1

#3rd try
min_gas_price = 1000000000
sum_gas_price = 0
for i in range(city_num-1):
    min_gas_price = min(min_gas_price, gas_price[i])
    sum_gas_price += min_gas_price*distance[i]
print(sum_gas_price)
