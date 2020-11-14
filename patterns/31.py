n=int(input(' number : '))
for i in range(n+1,0,-1):
    for j in range(i,n+1):
        print(' ',end=' ')
    for k in range(1,i):
        print(k,end=' ')
    print()