import time

inicio = time.perf_counter()

def union(pais, o, d):
	ro = find(pais, o)
	rd = find(pais, d)

	if(ro == rd):
		return False

	pais[rd - 1] = ro
	return True

def find(pais, x):
	while pais[x - 1] != x:
		x = pais[x - 1]
	return x

d, e = map(int, input().split(" "))
valor = 0
arestas = []
pais = [(x + 1) for x in range(d)]

for x in range(e):
	o, r, q = map(int, input().split(" "))

	arestas.append([o, r, q])

arestas.sort(key= lambda x: x[2])

for x in range(len(arestas)):

	if(len(arestas) == 0):
		break

	o = arestas[0][0]
	d = arestas[0][1]

	if(union(pais, o, d)):

		valor += arestas[0][2]
		arestas.pop(0)
		continue

	arestas.pop(0)

print(valor)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
