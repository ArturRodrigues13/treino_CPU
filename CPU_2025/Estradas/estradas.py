import time

inicio = time.perf_counter()

def union(pais, rank, o, d):
	ro = find(pais, o)
	rd = find(pais, d)

	if ro == rd:
		return False
	if rank[ro] < rank[rd]:
		pais[ro] = rd
	elif rank[ro] > rank[rd]:
		pais[rd] = ro
	else:
		pais[rd] = ro
		rank[ro] += 1

	return True

def find(pais, x):
	if pais[x] != x:
		pais[x] = find(pais, pais[x])
	return pais[x]

while True:
	try:
		v, a = map(int, input().split(" "))

		arestas = [None for _ in range(a)]
		arestas_esc = 0
		pais = [x for x in range(v)]
		rank = [0] * v
		preco = 0

		for x in range(a):
			o, d, val, c = input().split(" ")
			o = int(o)
			d = int(d)
			peso = float(val) - float(c)
			arestas[x] = [o - 1, d - 1, float(val), peso]

		arestas.sort(key=lambda x:x[3])

		for o, d, val, _ in arestas:

			if(arestas_esc == v - 1):
				break

			if(union(pais,rank, o, d)):
				preco += val
				arestas_esc += 1

		print(f"{preco:.2f}")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
