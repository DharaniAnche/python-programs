n=int(input('   number :    '))
num=1
inc=1
for i in range(n):
    print(' '*(n-i-1) + str(num)*inc,end=' ')
    num+=2#odd number
    inc+=2
    print()