import time

inicio = time.perf_counter()

def buscaCaminho(mapa:list, origem:int, destino:int, m_val: int, visitados=None):

	if visitados is None:
		visitados = set()

	visitados.add(origem)

	for vizinho in mapa[origem - 1]:
		no = vizinho[0]
		pont = vizinho[1]

		if(pont > m_val):
			m_val = pont

		if(no == destino):
			valores.append(m_val)

		if(no not in visitados):

			buscaCaminho(mapa, no, destino, m_val, visitados.copy())

	return None

while True:
	try:

		c, r = map(int, input().split(" "))

		caminhos = [[] for _ in range(c)]

		for x in range(r):
			o, d, p = map(int, input().split(" "))

			caminhos[o - 1].append((d, p))
			caminhos[d - 1].append((o, p))

		caminhos = [sorted(sublista, key= lambda x: x[1]) for sublista in caminhos]

		consul = int(input())

		for x in range(consul):

			valores = []

			i, f = map(int, input().split(" "))

			if(i == f):
				print(0)
				continue

			buscaCaminho(caminhos, i, f, 0)

			if(valores == []):
				print("IMPOSSIVEL")
				continue

			print(min(valores))

		print()

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
