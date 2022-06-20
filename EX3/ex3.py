'''
3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;
'''
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
	
