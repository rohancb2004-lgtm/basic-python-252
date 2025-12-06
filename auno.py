
x=int(input("enter a number"))
z=len(str(x))
y=x*x
if y%(10**z)==x:
    print("automorphic")
else:
    print("not automorphic