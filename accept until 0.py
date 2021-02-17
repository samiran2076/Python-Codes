'''WAP in C that accepts integers from the keyboard until the user
enters a zero or negative number. The program will output the number of positive
values entered the minimum value, the maximum value and the average of all the
entered numbers.'''

ele=int(input("enter number:"))
sum=0
counter=0
max=ele
min=ele
if(ele>0):
    while(ele>0):
        sum=sum+ele
        counter=counter+1
        if(ele>max):
            max=ele
        if(ele<min):
            min=ele
        ele=int(input("enter next:"))
else:
    print("negative number entered")


avg=sum/counter      
        
 
print(sum)
print(avg) 
print(max)
print(min)
      

