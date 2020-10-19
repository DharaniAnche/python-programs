#to check a given number is prime or not
n=int(input("enter a number : "))
if n<=1:
    print('its not a prime number!')
else:
    is_prime=True
    for i in range(2,n//2+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime==True:
        print(f'{n} is prime number')
    else:
        print(f'{n} is not a prime number')