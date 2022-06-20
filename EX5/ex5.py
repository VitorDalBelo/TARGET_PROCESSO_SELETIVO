string=input("Entre com uma string\n")

index= len(string)-1
result=""
while index>=0:
	result+=string[index]
	index-=1
	
print(result)
