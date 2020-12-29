def solution(cookie):
    len_cookie = len(cookie)
    num_cookie = 0
    for l in range(len_cookie):
        for r in range(len_cookie-1, l, -1):
            for m in range(l, r+1):
                #print(l,m,r)                
                #print(cookie[l:m+1], cookie[m+1:r+1])
                son1 = sum(cookie[l:m+1])
                son2 = sum(cookie[m+1:r+1])
                if(son1 == son2):
                    num_cookie = max(num_cookie, son1)

    #print(num_cookie)
    return num_cookie

solution([1,1,2,3])
'''
[1,1,2,3]	3
[1,2,4,5]	0
'''