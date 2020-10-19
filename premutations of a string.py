def perma(s):
    if len(s)<=1: return set(s)
    smaller = perma(s[1:])
    permutations=set()
    for ele in smaller:
        for pos in range(0,len(ele)+1):
            x = ele[pos:] + s[0] + ele[:pos]
            permutations.add(x)
    return permutations
print(perma('nana'))