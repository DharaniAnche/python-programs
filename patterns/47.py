n=int(input('enter a number : '))
for i in range(n,0,-1):
    print(' '*(n-i+1)+'* '*(i-1),end=' ')
    print()