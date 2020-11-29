s=input('Enter a string: ')
x=s.split()#seperates each word,stores in a list
x1=x[::-1]#reversing the list
print(' '.join(x1))