def solution(s):
    short_len = 1001
    
    if (len(s) == 1):
        return 1
    
    for i in range(1, len(s)//2 + 1):
        cnt = 0
        temp_s = ""
        for j in range(0, len(s)+1, i):
            if(temp_s[-i:] == s[j:j+i]):
                cnt += 1
            else:
                if(cnt > 1):
                    temp_s += str(cnt) + s[j:j+i]
                else:
                    temp_s += s[j:j+i]
                cnt = 1
        if(short_len > len(temp_s)):
            short_len = len(temp_s)

    return short_len

'''
"aabbaccc"	7
"ababcdcdababcdcd"	9
"abcabcdede"	8
"abcabcabcabcdededededede"	14
"xababcdcdababcdcd"	17
'''