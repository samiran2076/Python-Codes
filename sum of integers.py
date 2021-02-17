#WAP to calculate the sum of integers between 9 and 300
# inclusive which are divisible by 7 but not divisible by 63.
sum=0
count=0
for i in range(9,301):
    if(i%7==0 and i%63!=0):
        sum=sum+i
        count=count+1

print(sum)