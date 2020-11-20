n=int(input('enter a number : '))
inc=1
for i in range(1,n):
    for j in range(n,i,-1):
        print(' ',end=' ')
    for k in range(1,inc+1):
        print(chr(65+abs(k-i)),end=' ')
    inc+=2
    print()
