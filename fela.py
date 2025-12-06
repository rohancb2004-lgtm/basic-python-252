def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)




x=int(input("Enter a number  "))
y=fib(x)%100
print(y)
