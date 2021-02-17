
def lcm(a,b):
    if(a>b):
        greater=a
    else:
            greater=b
    while(1):    
        if(greater%a==0 and greater%b==0):
            lcm=greater
            break

        else:
            greater=greater+1
    print(lcm)

num1=int(input("num1:"))
num2=int(input("num1:"))
lcm(num1,num2)

