import time

inicio = time.perf_counter()

def busca_profundidade(grafo, no, buscado, visitados=None):

	if visitados is None:
		visitados = set()

	visitados.add(no)

	for vizinho in grafo.get(no, []):
		if vizinho not in visitados:
			b = busca_profundidade(grafo, vizinho, buscado, visitados)

	if(buscado in visitados):
		return True

	return False

grafos = {}

while True:
	try:
		grafos.clear()
		linha = [int(item) for item in input().split(" ")]
		for x in range(linha[1]):
			a, b = map(int, input().split())
			if(a not in grafos):
				grafos[a] = []
			grafos[a].append(b)
			if(b not in grafos):
				grafos[b] = []
			grafos[b].append(a)

		for x in range(linha[2]):
			a, b = map(int, input().split())
			b = busca_profundidade(grafos, a, b)

			if(b):
				print("TERRESTRE")
			else:
				print("MARITIMO")

		print()
	except EOFError:
		break

fim = time.perf_counter()

print(fim - inicio)
