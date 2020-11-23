n=int(input('enter a number : '))
for i in range(1,n):
    for j in range(n-1,i,-1):
        print(' ',end=' ')
    for k in range(i-1,-i,-1):
        print(chr(64+(i-abs(k))),end=' ')
    print()