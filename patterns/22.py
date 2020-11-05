n=int(input('enter the number : '))
for i in range(n,0,-1):
    for j in range(0,i):
        print(chr(64+i),end=' ')
    print()