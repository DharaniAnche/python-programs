n=int(input(' number : '))
for i in range(n,0,-1):
    for j in range(i,n):
        print(' ',end=' ')
    for k in range(0,i):
        print(chr(65+k),end=' ')
    print()