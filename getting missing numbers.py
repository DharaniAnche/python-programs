def get_missing_number(lst):
    return set(range(lst[len(lst)-1])[1:])-set(l)
l=list(range(1,101))
l.remove(99)
x=get_missing_number(l)
print(x)