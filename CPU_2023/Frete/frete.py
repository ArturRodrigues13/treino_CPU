import time
import heapq

inicio = time.perf_counter()

ilhas, pontes = map(int, input().split(" "))

mapa = [[] for _ in range(ilhas)]

armazena = [None for x in range(ilhas)]

for x in range(pontes):
	o, d, p = map(int, input().split(" "))

	mapa[o - 1].append((d, p))
	mapa[d - 1].append((o, p))

_, *sedes = [int(item) for item in input().split(" ")]

consul = int(input())

for x in range(consul):

	ilha_origem, slop, *destino = [int(item) for item in input().split(" ")]

	if(armazena[ilha_origem - 1] == None):

		distancias = {i: float('inf') for i in range(1, ilhas + 1)}
		distancias[ilha_origem] = 0
		fila_prioridade = [(0, ilha_origem)]

		while fila_prioridade:

			pedagio_atual, no_atual = heapq.heappop(fila_prioridade)

			if pedagio_atual > distancias[no_atual]:
				continue

			for vizinho, pedagio in mapa[no_atual - 1]:
				caminho = pedagio_atual + pedagio
				if caminho < distancias[vizinho]:
					distancias[vizinho] = caminho
					heapq.heappush(fila_prioridade, (caminho, vizinho))

		armazena[ilha_origem - 1] = distancias

	else:

		distancias = armazena[ilha_origem - 1]

	valores = {ilha: custo for ilha, custo in distancias.items() if ilha in destino}

	menor = min(valores, key=valores.get)

	print(menor, valores[menor])

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
