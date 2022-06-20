input_b=0
while True :
	try:
		input_b = int(input("Entre com o numero\n"))
		break
	except:
		print("Valor inválido")
		

sequencia = [0,1]

while len(sequencia)<11:
	size=len(sequencia)
	element=sequencia[size-2]+sequencia[size-1]
	sequencia.append(element)
	if input_b == element :
		print("O número ",input_b," esta contido na sequencia e é o ",size+1,"° elemento")
		print(sequencia)
		break
	elif  element > input_b:
		print("O número ",input_b," não esta contido na sequencia")
		break


