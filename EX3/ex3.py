import json
from operator import itemgetter
# Opening JSON file
jsonFile = open('dados.json')
  
# returns JSON object as 
# a dictionary
data = json.load(jsonFile)
#organiza em ordem crescente
dataSort = sorted(data, key=itemgetter('valor')) 

#remove os registros onde o velor é 0
for index in range(len(dataSort)-1):
	if dataSort[index]['valor'] !=0:
		dataSort=dataSort[slice(index, len(dataSort))]
		break
	elif index == len(dataSort)-1:
		dataSort=[]
		

if len(dataSort)==0:
	print("nenhum dia teve faturamento maior que 0")
else :
	soma=0
	for item in dataSort:
		soma+=item['valor']
	size=len(dataSort)
	media = soma / size
	acimaDaMedia = 0
	for item in dataSort:
		if item['valor'] > media :
			acimaDaMedia+=1
	print("O menor valor foi ",dataSort[0]['valor']," no dia ",dataSort[0]['dia'])
	print("O maior valor foi ",dataSort[size-1]['valor']," no dia ",dataSort[size-1]['dia'])
	print("Houve  ",acimaDaMedia," dias com o valor acima da média")
	
