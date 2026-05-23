import time

inicio = time.perf_counter()

q1, q2 = [int(item) for item in input().split(" ")]
datas = []
filmes = []

for x in range(q1):
	filme = input().split(" (")
	filme[1] = filme[1].replace(")"," ")
	datas.append(int(filme[1]))
	filmes.append(filme[0])

for x in range(q2):

	consulta = [int(item) for item in input().split(" ")]

	if(len(consulta) == 2):

		indices = [i for i, valor in enumerate(datas) if valor >= consulta[0] and valor <= consulta[1]]

		if(len(indices) == 0):
			print("Entre Trabalhos")
			print()
			continue

		print(*[filmes[i] for i in indices], sep="\n")
		print()

	else:
		indices = [i for i, valor in enumerate(datas) if valor == consulta[0]]

		if(len(indices) == 0):
			print("Entre Trabalhos")
			print()
			continue

		print(*[filmes[i] for i in indices], sep="\n")
		print()

fim = time.perf_counter()

print(fim - inicio)
