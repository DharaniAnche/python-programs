n=int(input('number : '))
inc=7
for i in range(n,0,-1):
    print(' '*(n-i+1)+str(inc)*(inc),end=' ')
    inc-=2
    print()