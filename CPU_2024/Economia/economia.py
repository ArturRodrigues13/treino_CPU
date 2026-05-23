import time

inicio = time.perf_counter()

while True:

	q = int(input())
	marcas = []
	valores = []

	if(q == 0):
		break

	for x in range(q):
		linha = input().split(" ")
		marcas.append(linha[0])
		conta = float(linha[3]) / (float(linha[1]) * float(linha[2]))
		conta = round(conta, 5)
		valores.append(conta)

	min_v = min(valores)
	indices = [i for i, valor in enumerate(valores) if valor == min_v]

	if(len(indices) == 1):
		print(marcas[indices[0]])
		print()
	else:
		ordena = [marcas[i] for i in indices]
		ordena.sort()
		print(*[ordena[i] for i in range(len(ordena))],sep="\n")
		print()

fim = time.perf_counter()

print(fim - inicio)
