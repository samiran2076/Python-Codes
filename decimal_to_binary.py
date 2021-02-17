a=int(input("decimal number:"))
b=bin(a).replace("0b","")
print(b)

# Function to convert decimal number to binary using recursion
def DecimalToBinary(num):
	
	if num >= 1:
		DecimalToBinary(num // 2)
	print(num % 2, end = '')

# Driver Code
if __name__ == '__main__':
	dec_val = 24
	DecimalToBinary(dec_val)
