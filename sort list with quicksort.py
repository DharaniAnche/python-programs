def qsort(L):
    if L == []: return []
    return qsort([x for x in L[1:] if x < L[0]]) + L[0:1] + qsort([x for x in L[1:] if x>=L[0]])
L=[44,34,67,23,87,45,24]
x=qsort(L)
print(x)