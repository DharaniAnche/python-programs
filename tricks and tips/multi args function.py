#function that takes as many inputs as users wants
#user desired number of arguments - multi-args
def addition(*num):
    #normal way
    res=0
    for i in num:
        res=res+i
    return res
def add(*num):
    #using list_comprehension and walrus operator
    total = 0
    return [total := total + x for x in num].pop()#returns last element in a list
if __name__=='__main__':
    print(f'by 1st method {addition(1,2,4,5,6,7,8,9,0,10)}')
    print(f'by 2nd method {add(1,2)}')