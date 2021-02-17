#fibbonaci series
##a= int(input("enter the term of fibonnaci series:"))
"""sum=0
a=0
b=1
n=int(input("enter the number of terms:"))
count=0
while(count<n):
    count=count+1
    print(a)
    sum=a+b
    a=b
    b=sum
    
'print(sum)'
print(count)"""

def fibonnaci(n):
    sum=0
    a=0
    b=1
    n=int(input("enter the number of terms:"))
    count=0
    while(count<n):
        count=count+1
        print(a)
        sum=a+b
        a=b
        b=sum
fibonnaci(5)

    
