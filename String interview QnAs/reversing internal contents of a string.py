s=input('Enter any string: ')
x=s.split()
y=[]
for each_word in x:
    y.append(each_word[::-1])
outP=' '.join(y)
print(outP)