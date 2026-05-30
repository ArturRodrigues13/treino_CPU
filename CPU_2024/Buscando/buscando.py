import time

inicio = time.perf_counter()

def buscaLargura(lista:list, no:int, buscado:int):

	visitados = set()
	visitados.add(no)
	fila = [[no, 0]]

	while len(fila) > 0:
		v, dist = fila.pop(0)

		if(v == buscado):
			if(v == no):
				return - 1
			return dist - 1

		for x in lista[v - 1]:
			if(x not in visitados):
				visitados.add(x)
				fila.append([x, dist + 1])
	return -1

while True:
	try:
		c, r = map(int, input().split(" "))

		conexoes = [[] for _ in range(c)]

		for x in range(r):
			o, d = map(int, input().split(" "))

			conexoes[o - 1].append(d)
			conexoes[d - 1].append(o)

		consul = int(input())

		for x in range(consul):
			o, d = map(int, input().split(" "))
			res = buscaLargura(conexoes, o, d)
			if(res != - 1):
				print(res)
			else:
				print("IMPOSSIVEL")

		print()

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
