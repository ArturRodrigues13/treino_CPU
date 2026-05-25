import time

inicio = time.perf_counter()

escopoAtual = 0
variaveis = {}

valido = True

linha = input()

for x in range(len(linha)):
	if(linha[x] == "["):
		escopoAtual +=1
	elif(linha[x] == "D"):
		variaveis[linha[x + 1]] = escopoAtual
	elif(linha[x] == "A"):
		if(linha[x + 1] in variaveis):
			if not (variaveis[linha[x + 1]] <= escopoAtual):
				valido = False
				break
		else:
			valido = False
	elif(linha[x] == "]"):
		escopoAtual -= 1

if(valido):
	print("Semanticamente correto!")
else:
	print("Erro de escopo!")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
