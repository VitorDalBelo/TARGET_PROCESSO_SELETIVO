'''
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;
'''

string=input("Entre com uma string\n")

index= len(string)-1
result=""
while index>=0:
	result+=string[index]
	index-=1
	
print(result)
