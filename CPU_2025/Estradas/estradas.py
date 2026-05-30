import time

inicio = time.perf_counter()

def union(pais, o, d):
	ro = find(pais, o)
	rd = find(pais, d)

	if ro == rd:
		return False

	pais[rd - 1] = ro
	return True

def find(pais, x):
	while pais[x - 1] != x:
		x = pais[x - 1]
	return x

while True:
	try:
		v, a = map(int, input().split(" "))

		arestas = [None for _ in range(a)]
		arestas_esc = []
		pais = [x + 1 for x in range(v)]
		preco = []

		for x in range(a):
			o, d, v, c = input().split(" ")
			o = int(o)
			d = int(d)
			peso = float(v) - float(c)
			arestas[x] = [o, d, float(v), peso]

		arestas.sort(key=lambda x:x[3])

		while True:

			if(len(arestas) == 0):
				break

			origem = arestas[0][0]
			destino = arestas[0][1]

			if(union(pais, origem, destino)):
				preco.append(arestas[0][2])
				arestas_esc.append(arestas[0])
				arestas.pop(0)
				continue

			arestas.pop(0)

		soma = sum(preco)

		print(f"{soma:.2f}")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
