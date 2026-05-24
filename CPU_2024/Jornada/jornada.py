import time

inicio = time.perf_counter()

total = []

def busca(grafo, no, valor):

	val = valor + premios[no - 1]

	if(no not in grafo):
		total.append(val)
		return

	filhos = grafo.get(no)

	for sala in filhos:
		busca(grafo, sala, val)

	return

grafos = {}
premios = []

while True:

	premios.clear()
	grafos.clear()
	total.clear()

	salas, premio = input().split(" ")

	if(salas == '0' and premio == '0'):
		break

	premios.append(float(premio))

	for x in range(int(salas) - 1):
		val = x + 2
		a, b = input().split(" ")
		a = int(a)
		if(a not in grafos):
			grafos[a] = []

		grafos[a].append(val)

		premios.append(float(b))

	busca(grafos, 1, 0)

	print(f"{max(total):.2f}")

fim = time.perf_counter()

print(fim - inicio)
