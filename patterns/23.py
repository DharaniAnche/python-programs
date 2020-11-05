n=int(input('enter a number '))
for i in range(n+1):
    for j in range(n-1,i-1,-1):
        print(chr(j+65),end=' ')
    print()