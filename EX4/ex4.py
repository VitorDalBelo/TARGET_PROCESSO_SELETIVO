'''
4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.
'''


dados=[
	{'uf':"SP",'valor':67836.43},
	{'uf':"RJ",'valor':36678.66},
	{'uf':"MG",'valor':29229.88},
	{'uf':"ES",'valor':27165.48},
	{'uf':"Outros",'valor':19849.53},
]
soma=0
for dado in dados:
	soma+=dado["valor"]
	
print("Total: ",soma)
for dado in dados:
	print("UF: ",dado["uf"]," Valor: ",dado["valor"]," Percentual: ",round((dado["valor"]/soma)*100,2),"%")
	
