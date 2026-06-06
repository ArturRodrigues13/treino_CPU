import time

inicio = time.perf_counter()

while True:

	try:

		n, *jogadores = [int(item) for item in input().split()]

		quant_pares = n - 1

		pares = []
		valores = []
		pontuacao = 0

		for x in range(quant_pares):
			pares.append([jogadores[x],jogadores[x + 1]])
			valores.append(jogadores[x] + jogadores[x + 1])

		for x in range(n // 2):
			if(x == n / 2 - 2):
				pontuacao += max(valores)
				break

			maior = max(valores)
			index = valores.index(maior)

			if(index == 0):

				pares.pop(index + 1)
				pares.pop(index)
				valores.pop(index + 1)
				valores.pop(index)

			elif(index == len(pares) - 1):

				pares.pop(index)
				pares.pop(index - 1)
				valores.pop(index)
				valores.pop(index - 1)

			else:

				valores[index] = pares[index - 1][0] + pares[index + 1][1]
				valores.pop(index + 1)
				valores.pop(index - 1)

				pares[index] = [pares[index - 1][0], pares[index + 1][1]]

				pares.pop(index + 1)
				pares.pop(index - 1)

			if(x % 2 == 0):
				pontuacao += maior

		print(pontuacao)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
