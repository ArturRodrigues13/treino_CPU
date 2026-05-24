import time

inicio = time.perf_counter()

alegobois = [int(item) for item in input().split(" ")]

pesos = [int(item) for item in input().split(" ")]

bois = []

for x in range(alegobois[1]):

	boi = []
	nome, *notas = input().split(" ")
	boi.append(nome)
	notas = [float(item) for item in notas]
	boi.append(notas)
	boi.append(sum(x * p for (x, p) in zip(notas, pesos)))
	bois.append(boi)

bois.sort(key=lambda x:(x[2],*[i for i in x[1]]),reverse=True)

print(*[nome[0] for nome in bois],sep="\n")

fim = time.perf_counter()
