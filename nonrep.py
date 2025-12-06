lst = [4,5,5,3,5,6,7,4,3,6]
x=len(lst)
for i in range(x):
    y=0
    for j in lst:
        if lst[i]==j:
            y=y+1
    if y==1:
        print(lst[i])
