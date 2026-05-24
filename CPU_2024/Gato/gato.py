import time

inicio = time.perf_counter()

visitados = []

def busca(grafo, no):

	for ramo in grafo.get(no, []):

		if(no in grafo[ramo]):
			grafo[ramo].remove(no)

		if(ramo in visitados):
			return False

		visitados.append(ramo)
		b = busca(grafo, ramo)

	return True

grafos = {}

while True:

	grafos.clear()
	visitados.clear()
	arvore = True

	try:
		n, *linha = input().split(" ")
		n = int(n)

		for x in range(n - 1):
			linha[x] = linha[x].replace("{","")
			linha[x] = linha[x].replace(","," ")
			linha[x] = linha[x].replace("}","")
			line = linha[x].split(" ")
			a, b = map(int, line)

			if(a not in grafos):
				grafos[a] = []
			grafos[a].append(b)

			if(b not in grafos):
				grafos[b] = []
			grafos[b].append(a)

		if(n in grafos):
			visitados.append(n)
			arvore = busca(grafos,n)
		else:
			arvore = False

		if(len(visitados) < n):
			arvore = False

		if(n == 1):
			arvore = True

		if(arvore):
			print("OK")
		else:
			print("Miau")


	except EOFError:
		break



fim = time.perf_counter()

print(fim - inicio)
