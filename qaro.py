import math
a=int(input("Enter a number of x^2: "))
b=int(input("Enter a number of x: "))
c=int(input("Enter a number of constant: "))
x=0
x=b*b-4*a*c
if x>0:
    x1=(-b+math.sqrt(x))//(2*a)
    x2=(-b-math.sqrt(x))//(2*a)
    print(x1,x2)
elif x==0:
    x1=(-b+math.sqrt(x))//(2*a)
    x2=(b-math.sqrt(x))//(2*a)
    print(x1,x2)
elif x<0:
    print("complex roots")

