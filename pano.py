x=int(input("Enter a number  "))
r=0
while x!=0:
    l= x%10
    r=r*10 + l
    x= x//10
if x == r:
    print("palindrome")
else:
    print("not palindrome")
