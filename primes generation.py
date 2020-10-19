n=int(input('enter a number : '))
n1=2
while n1<=n:
    #code to check n1 is prime or not
    is_prime=True
    for i in range(2,n1//2+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(n1)
    n1=n1+1
    