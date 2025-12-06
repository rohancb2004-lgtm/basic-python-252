x= [3,0,1]
sum1=0
sum2=0
for i in x:
    sum1+=i
for j in range(len(x)+1):
    sum2=sum2+j
print(sum2-sum1)