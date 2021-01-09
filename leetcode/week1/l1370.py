def sortString(s):
    answer = []
    sentence = list(s)
    sentence.sort()
    d = {}
    for _ in sentence:
        if _ not in d:
            d[_] = 1
        else:
            d[_] += 1

    while d != {}:
        keys_in = list(d.keys())
        keys_in.sort()
        #increasing steps
        for key in keys_in:
            answer.append(key)
            if d[key] == 1:
                d.pop(key)
            else:
                d[key] -= 1
        
        keys_de = list(d.keys())
        keys_de.sort(reverse=True)
        #increasing steps
        for key in keys_de:
            answer.append(key)
            if d[key] == 1:
                d.pop(key)
            else:
                d[key] -= 1
    
    return ''.join(answer)

print(sortString("aaaabbbbcccc"))