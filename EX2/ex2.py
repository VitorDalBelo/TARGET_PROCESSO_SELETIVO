'''
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
'''
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


