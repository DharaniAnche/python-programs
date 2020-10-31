n=int(input('enter a number : '))
for i in range(n):
    for j in range(i+1):
        print(chr(64+j+1),end=' ')
    print()