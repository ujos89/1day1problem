def find_children(skills, parent):
    temp = []
    for rel in skills:
        if(rel[0] == parent):
            temp.append(rel[1])

    answer= [parent]
    answer.append(temp)
    return answer

def leaf_num(skills, root):
    temp_tree = find_children(skills, root)
    if ( temp_tree[1] ):
        return 1
    else:
        for temp_root in temp_tree[1]:
            num += leaf_num(skills, temp_root)
            return num


def solution(total_sp, skills):
    #find root
    find_root = [i for i in range(1, len(skills)+1)]
    for idx in range(len(skills)):
        if skills[idx][1] in find_root:
            find_root.remove(skills[idx][1])
    root = find_root[0]
    
    rel = find_root
    tree = []
    
    for root in rel:
        temp_rel = find_children(skills, root)
        tree.append(temp_rel)
        print(temp_rel, tree)

    '''
    while(skills):
        print(rel)
        for root in rel:
            temp_rel = find_children(skills, root)
            tree.append(temp_rel)
            print(temp_rel, tree)
        
        rel = temp_rel[1]
    '''




    
    

    answer = []
    return answer

find_children([[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]], 1)
solution(121,	[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]])

#121	[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]	[44, 11, 33, 11, 11, 11]