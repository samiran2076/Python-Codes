def leapyear(n):
    #n=int(input("enter the year:"))
    if(n%400==0):
        print("leap year")
    elif(n%100==0):
        print("not a leap year")
    elif(n%4==0):
        print("leap year")
    else:
        print("not ")

year=int(input("enter year"))
leapyear(year)

