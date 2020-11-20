n=int(input('enter a number : '))
inc=1
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print(' ',end='')
    for k in range(inc,0,-1):
        print(k,end='')
    inc+=2
    print()