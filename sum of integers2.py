'''WAP in C that accepts a positive integer n less than 50 from the user
and prints out the sum 1^4 + 2^4+ 3^4+ 4^4+ ... + n^4. If the input is outside the range,
the program should terminate with an appropriate message.'''

sum=0
count=0
a=int(input("enter number:"))
if(a>50):
    print("limit exceeded")
else:
    for i in range(1,a+1):
        sum=sum+(i**4)
        count=count+1
    
    print(sum)