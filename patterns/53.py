n=int(input('enter a num : '))
inc=7
for i in range(n,0,-1):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(1,inc+1):
        print(chr(64+k),end=' ')
    inc-=2
    print()