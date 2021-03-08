import sys
import copy
from itertools import permutations

def inputdata():
    input = sys.stdin.readline
    n = int(input())
    expr = list(input().strip())
    return n, expr

def cal(a_idx ,b_idx ,op_idx, expression):
    a, b, operator = expression[a_idx], expression[b_idx], expression[op_idx]
    if operator == '+':
        return int(a)+int(b)
    elif operator == '-':
        return int(a)-int(b)
    elif operator == '*':
        return int(a)*int(b)

def main():
    #input
    n, expr = inputdata()
    
    # #maximum number of operatior: 10, brute force(10!)
    # answer = -2**31
    # operator_num = n//2
    # for p in permutations(range(operator_num)):
    #     tmp_expr = copy.copy(expr)
    #     for _ in p:
    #         a_idx, b_idx, op_idx = _*2, _*2+2, _*2+1
    #         tmp_cal = cal(a_idx, b_idx, op_idx, tmp_expr)
    #         tmp_expr[a_idx] = tmp_expr[b_idx] = tmp_cal

    #     if tmp_cal > answer:
    #         answer = tmp_cal
    
    # print(answer)
    # time-over; consider nesscesray case (misunderstand use of parentheses)

    answer = -2**31
    operator_num = n//2
    p_num = (operator_num+1)//2

    for p in permutations(range(operator_num)):
        tmp_expr = copy.copy(expr)
        for _ in p:
            a_idx, b_idx, op_idx = _*2, _*2+2, _*2+1
            tmp_cal = cal(a_idx, b_idx, op_idx, tmp_expr)
            tmp_expr[a_idx] = tmp_expr[b_idx] = tmp_cal

        if tmp_cal > answer:
            answer = tmp_cal
    
    print(answer)
    

if __name__== "__main__":
    main()