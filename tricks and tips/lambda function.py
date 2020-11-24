#anonymous function - no name functions
#normal way
def add(a,b):
    return a+b
if __name__=='__main__':
    print(f'using normal way: {add(5,6)}')
    #using lambda
    addition=lambda a,b:a+b
    print(f'using lambda func: {addition(5,6)}')