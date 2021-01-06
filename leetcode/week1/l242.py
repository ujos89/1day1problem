s = str(input())
t = str(input())

def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    t = list(t)
    for _ in s:
        if _ not in t:
            return False
        else:
            t.remove(_)
    
    return True

print(isAnagram(s, t))
