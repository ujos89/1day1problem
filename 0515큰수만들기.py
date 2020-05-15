import copy
def list2num(arr):
    temp = 0
    for i in range(len(arr)):
        temp += arr[i] * ( 10 ** (len(arr)-1-i) )
    return temp


def solution(number, k):
    num = list(map(int,number))

    for i in range(k):
        temp_max = 0
        del_idx = -1

        for j in range(len(num)):
            temp_list = copy.deepcopy(num)
            del temp_list[j]
            if ( list2num(temp_list) > temp_max ):
                temp_max = list2num(temp_list)
                del_idx = j
        del num[del_idx]
        
    answer = ""
    for i in num:
        answer += str(i)

    return answer

solution("1924",2)
solution("1231234",3)
solution("4177252841",4)