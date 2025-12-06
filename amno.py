x=int(input("enter a number: "))
y=x
z=0
while y!= 0:
    r=y % 10
    z=z+r**3
    y=y//10
if z==x:
    print("amstrong")
else:
    print("not amstrong")