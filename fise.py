def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)




x=int(input("Enter a number  "))
print(fib(x))
#
# a,b=0,1
# for i in range(x):
#     print(a)
#     a,b=b,a+b

