x=int(input("Enter a number: "))
y=0
for i in range(x):
        r=x%10
        y=y+r
        x=x//10
print(y)
