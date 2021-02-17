'''A perfect number is a positive number in which sum of all positive
divisors excluding that number is equal to that number. For example, 8128 is a
perfect number. WAP in C to accept a positive integer from user and check
whether it is a perfect number or not.'''

sum=0
count=0
a=int(input("enter the number:"))
for i in range(1,a):
    if(a%i==0):
        sum=sum+i
        count=count+1

if(a==sum):
    print("perfect number:",a)
else:
    print("not")