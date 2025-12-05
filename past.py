x=input("Enter a string  ").lower()
x = x.replace(' ','')
if x== x[::-1]:
    print("palindrome")
else:
    print("not palindrome")
