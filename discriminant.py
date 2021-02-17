a=int(input("enter a"))
b=int(input("enter b"))
c=int(input("enter c"))
d=((b*b)-4*a*c)
if(d>0):
    print("real and unequal")
elif(d==0):
    print("real and equal")
elif(d<0):
    print("imaginaryy")
