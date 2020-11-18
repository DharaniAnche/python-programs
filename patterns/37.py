n=int(input('number : '))
inc=1
for i in range(n):
        print(' '*(n-i-1)+chr(65+i)*inc,end=' ')
            inc+=2
                print()
