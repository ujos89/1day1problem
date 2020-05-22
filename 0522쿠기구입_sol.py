def solution(cookie):
    num_cookie = 0
    for m in range(len(cookie)-1):
        son1, idx_son1 = cookie[m], m
        son2, idx_son2 = cookie[m+1], m+1

        while(True):
            if(son1 == son2 and son1 > num_cookie):
                num_cookie = son1
            elif(son1 >= son2 and idx_son2 < len(cookie)-1 ):
                idx_son2 += 1
                son2 += cookie[idx_son2]
            elif(son1 <= son2 and idx_son1 > 0 ):
                idx_son1 -= 1
                son1 += cookie[idx_son1]
            else:
                break

    #print(num_cookie)
    return num_cookie

solution([1,1,2,3])