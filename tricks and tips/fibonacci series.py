fibo=lambda n:n if n<=1 else fibo(n-1)+fibo(n-2)
n=input()
print(fibo(int(n)))