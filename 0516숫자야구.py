from itertools import permutations

def baseball_check(ans, num, strike, ball):
    s = 0
    b = 0

    ans_list = [int(i) for i in str(ans)]
    num_list = [int(i) for i in str(num)]
    for idx_ans in range(len(ans_list)):
        for idx_num in range(len(num_list)):
            if( ans_list[idx_ans] == num_list[idx_num] ):
                if(idx_ans == idx_num):
                    s += 1
                else:
                    b += 1
    if( s == strike and b == ball):
        return False
    else:
        return True


def solution(baseball):
    per = list(permutations(range(1,10), 3))
    cand = []
    for i in range(len(per)):
        temp_num = 100 * int(per[i][0]) + 10 * int(per[i][1]) + int(per[i][2])
        cand.append(temp_num)
 
    for i in range(len(baseball)):
        for j in range(len(cand)-1, -1, -1):

            if( baseball_check(cand[j], baseball[i][0], baseball[i][1], baseball[i][2]) ):
                del cand[j]
    #print(cand)
    return len(cand)


#print(baseball_check(124,125,2,0))
solution ([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])
#[[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]	2