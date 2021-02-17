n=int(input("enter number:"))
count=0
print("The prime factors are:")
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
        print(i)
if(count==2):
    print("prime")