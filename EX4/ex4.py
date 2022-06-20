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
	
