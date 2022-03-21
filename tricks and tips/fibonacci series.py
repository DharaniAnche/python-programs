fibo=lambda n:n if n<=1 else fibo(n-1)+fibo(n-2)
n=input()
print(fibo(int(n)))

fib=[0,1]
sum=0
for i in range(15):
    sum=fib[i]+fib[i+1]
    fib.append(sum)
print(fib)