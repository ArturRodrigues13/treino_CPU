import time

inicio = time.perf_counter()

linha = [int(item) for item in input().split(" ")]

alfabeto = []
estado_atual = 0

alfabeto = input()
alfabeto = list(alfabeto)

transicoes = []

for x in range(linha[1]):
	transicoes.append([int(item) for item in input().split(" ")])

aceitacao = [int(item) for item in input().split(" ")]

for x in range(linha[2]):
	estado_atual = 0
	cadeia = input()
	cadeia = list(cadeia)
	if not (cadeia == ['*']):
		for y in range(len(cadeia)):
			indice = alfabeto.index(cadeia[y])
			estado_atual = transicoes[indice][estado_atual]

	if(aceitacao[estado_atual] == 1):
		print("Aceita")
	else:
		print("Rejeita")

fim = time.perf_counter()

print(fim - inicio)
