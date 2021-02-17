
import math
a1=int(input("abscissa of A:"))
a2=int(input("ordinate of A:"))
b1=int(input("abscissa of B:"))
b2=int(input("ordinate of B:"))
d2=((b2-a2)**2)+((b1-a1)**2)
d=math.sqrt(d2)
print(d)
m1=(a1+b1)/2
m2=(a2+b2)/2
print(m1,m2)
       