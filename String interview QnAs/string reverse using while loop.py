s=input('Enter a string: ')
x=''
i=len(s)-1
while i>=0:
    x=x+s[i]
    i-=1
print(x)