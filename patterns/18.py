n=int(input('number : '))
for i in range(n):
    print(chr(65+i)*(n-i),end=' ')
    print()