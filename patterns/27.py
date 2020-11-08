n=int(input('enter a number : '))
for i in range(n):
    for j in range(n-1,i,-1):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(64+i),end=' ')
    print()