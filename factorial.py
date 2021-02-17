'''WAP in C to accept a nonnegative number from the user and prints
out the factorial of the given input.'''
mul=1
a=int(input("enter the number:"))
if(a<0):
    print("get your basiccs clear")
elif(a==0 or a==1):
    print("1")
for i in range(a,0,-1):
    mul=mul*i
    print(mul)