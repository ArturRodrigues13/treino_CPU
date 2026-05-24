import time

inicio = time.perf_counter()

alegobois = [int(item) for item in input().split(" ")]

pesos = [int(item) for item in input().split(" ")]

bois = []
notas = [0] * alegobois[1]

maior = 0
i_maior = 0

apresentacoes = []

for x in range(alegobois[1]):

	b, *apresentacao = input().split(" ")
	bois.append(b)
	apresentacao = [float(item) for item in apresentacao]
	apresentacoes.append(apresentacao)

	for y in range(alegobois[0]):
		notas[x] += apresentacao[y] * pesos[y]

while True:

	if(len(bois) == 0):
		break

	maior = max(notas)
	i_maior = notas.index(maior)

	if(notas.count(maior) > 1):
		indices = [i for i, valor in enumerate(notas) if valor == maior]
		empatados = [[bois[i], apresentacoes[i]] for i in indices]
		empatados.sort(key=lambda x:(x[1]),reverse=True)
		print(*[e[0] for e in empatados],sep="\n")
		bois = [b for (i, b) in enumerate(bois) if i not in indices]
		notas = [n for (i, n) in enumerate(notas) if i not in indices]
		apresentacoes = [a for (i, a) in enumerate(apresentacoes) if i not in indices]

	else:
		print(bois[i_maior])
		bois.pop(i_maior)
		apresentacoes.pop(i_maior)
		notas.pop(i_maior)

fim = time.perf_counter()
