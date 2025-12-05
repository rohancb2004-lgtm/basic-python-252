x=int(input("Enter a string  "))
for i in range(x):
    for j in range(i):
        print(i,end="")
    print()

1
22
333
4444
55555

x=int(input("Enter a string  "))
for i in range(x,0,-1):
    for j in range(i):
        print(x,end="")
    print()

55555
5555
555
55
5

x=int(input("Enter a string  "))
for i in range(x):
    for j in range(x-i,0,-1):
        print(i,end="")
    print()
00000
1111
222
33
4


x = int(input("Enter a string  "))
y=1
for i in range(1,x+1):
    for j in range(i):
        print(y,end="")
    print()
    y=y+2
1
33
555
7777
