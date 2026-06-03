import time

inicio = time.perf_counter()

def BFS(grafo:list, origem:int, destino:int, pais:list):

	visitados = [False]*(destino + 1)

	fila = []

	fila.append(origem)
	visitados[origem] = True

	while fila:

		atual = fila.pop(0)

		for ind, val in enumerate(grafo[atual]):
			if visitados[ind] == False and val > 0:
				fila.append(ind)
				visitados[ind] = True
				pais[ind] = atual
				if ind == destino:
					return True

	return False

def FordFulkerson(grafo:list, origem:int, destino:int):

	pais = [-1]*(destino + 1)

	fluxo_max = 0

	while BFS(grafo, origem, destino, pais) :

		fluxo_caminho = float("Inf")
		s = destino
		while(s !=  origem):
			fluxo_caminho = min (fluxo_caminho,grafo[pais[s]][s])
			s = pais[s]

		fluxo_max += fluxo_caminho

		s = destino
		while(s !=  origem):
			u = pais[s]
			grafo[u][s] -= fluxo_caminho
			grafo[s][u] += fluxo_caminho
			s = pais[s]

	return fluxo_max

while True:

	try:
		v, a = map(int, input().split(" "))

		maq = [[0 for _ in range(v)] for _ in range(v)]

		for x in range(a):
			o, d, f = map(int, input().split(" "))
			maq[o - 1][d - 1] = f

		maq_c = maq.copy()
		fluxo_max = FordFulkerson(maq_c, 0, v - 1)
		print(fluxo_max)

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
