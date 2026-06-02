import time
import math

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

def calcDist(x1, y1, x2, y2):
	return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))

while True:

	c, l, v = map(int, input().split())

	if(c == 0 and l == 0 and v == 0):
		break

	vertices = []
	jardim_a = []
	arestas_esc = []
	pais = [x + 1 for x in range(v + 1)]
	vertices.append((0, 0.0, 0.0))

	for x in range(v):
		x, y = map(float, input().split())
		vertices.append((x + 1, x, y))

	for i in range(v + 1):
		x1 = vertices[i][1]
		y1 = vertices[i][2]
		for j in range(v + 1):
			if i == j:
				continue
			dist = calcDist(x1, y1, vertices[j][1], vertices[j][2])
			jardim_a.append((i, j, dist))

	jardim_a.sort(key= lambda x: x[2])

	comp = 0

	while True:

		if(len(jardim_a) == 0):
			break

		origem = jardim_a[0][0]
		destino = jardim_a[0][1]

		if(union(pais, origem, destino)):
			comp += jardim_a[0][2]
			arestas_esc.append(jardim_a[0])
			jardim_a.pop(0)
			continue

		jardim_a.pop(0)

	print(f"{comp:.2f}")

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
