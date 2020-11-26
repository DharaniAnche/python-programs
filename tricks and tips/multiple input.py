#taking multiple inputs & assigning them with one input and one split function
#normal way
x=input("enter 1st number")
y=input("enter 2nd number")
print(x)
print(y)
#python trick
#if split() is empty it takes space as separator or you can specify a separator
x,y=input("enter two values: ").split()
