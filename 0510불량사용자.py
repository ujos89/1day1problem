from itertools import permutations

def solution(user_id, banned_id):
    candidate_list = list(permutations(user_id, len(banned_id)))

    ban_list = []
    for cand_idx in range(len(candidate_list)):
        cand_check = 0

        for ban_idx in range(len(banned_id)):
            ban_check = 0
            if(len(banned_id[ban_idx]) == len(candidate_list[cand_idx][ban_idx])):
                for i in range(len(banned_id[ban_idx])):
                    if(banned_id[ban_idx][i] == '*' or banned_id[ban_idx][i] == candidate_list[cand_idx][ban_idx][i]):
                        ban_check += 1
                
            if(ban_check == len(banned_id[ban_idx])):
                cand_check += 1
        if(cand_check == len(banned_id) and sorted(candidate_list[cand_idx]) not in ban_list):
            ban_list.append(sorted(candidate_list[cand_idx]))

    return len(ban_list)

solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]	)
solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])