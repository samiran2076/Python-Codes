'''Write a program in C to accept any integer from the user and display
whether the number is a Armstrong number or not.'''

sum=0
a=int(input("enter the number"))
cpy=a
while(a>0):
    tmp=a%10
    sum=sum+(tmp**3)
    a=a//10
print(sum,"=",cpy)

if(sum==cpy):
    print("Armstrong Number")
else:
    print("Not")
    
    