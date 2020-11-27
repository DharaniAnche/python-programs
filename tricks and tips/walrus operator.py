#warlus is a new operator in python3.8
#allows assignment direclty in the experssion
#normal way
x=[1,2,3]
n=len(x)
if n>2:
    print(n)
#using warlus operator
y=[4,5,6]
if(n:=len(y)>2):
    print(n)