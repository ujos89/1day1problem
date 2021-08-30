def solution(new_id):
    # step1
    new_id = new_id.lower()
    
    # step2
    new_id2 = []
    for letter in new_id:
        if letter.islower() or letter.isdecimal() or letter=='-' or letter=='.' or letter=='_':
            new_id2.append(letter)

    # step3
    del_idx = []
    for idx in range(len(new_id2)-1):
        now_pos, nxt_pos = new_id2[idx], new_id2[idx+1]
        if now_pos == nxt_pos == '.':
            del_idx.append(idx)        
    del_idx.reverse()
    for idx in del_idx:
        del new_id2[idx]

    print(new_id2)
    # step4
    if len(new_id2) < 2:
        if new_id2[0]=='.':
            del new_id2[0]
    else:
        if new_id2[-1]=='.':
            del new_id2[-1]
        if new_id2[0]=='.':
            del new_id2[0]
        
    # step5
    if not new_id2:
        new_id2.append('a')

    # step6
    if len(new_id2) >= 16:
        new_id2 = new_id2[:15]
        if new_id2[-1] == '.':
            del new_id2[-1]

    # step7
    if len(new_id2) <= 2:
        for _ in range(3-len(new_id2)):
            new_id2.append(new_id2[-1])

    answer = ''.join(new_id2)
    return answer

# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("cc"))
solution("abcdefghijklmn.p")
solution("=.=")