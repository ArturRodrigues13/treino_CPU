import time

def igual():
	print("igual")

inicio = time.perf_counter()

with open("Boi/entrada.txt","r") as file:
	conteudo = file.read().splitlines()

alegobois = conteudo[0].split(" ")
alegobois = [int(item) for item in alegobois]

pesos = conteudo[1].split(" ")
pesos = [int(item) for item in pesos]

bois = []
notas = [0] * alegobois[0]

maior = 0
i_maior = 0

apresentacoes = []

desempate = []

for x in range(alegobois[1]):

	apresentacao = conteudo[x + 2].split(" ")
	bois.insert(x, apresentacao[0])
	apresentacao.pop(0)
	apresentacao = [float(item) for item in apresentacao]
	apresentacoes.append(apresentacao)

	for y in range(alegobois[0]):
		notas[x] += apresentacao[y] * pesos[y]

	notas[x] = notas[x] / sum(pesos)



for i in range(len(bois)):

	maior = max(notas)
	i_maior = notas.index(maior)

	if(notas.count(notas[i_maior]) > 1):
		print("Bad Ending")

	else:
		print(bois[i_maior])
		bois.pop(i_maior)
		apresentacoes.pop(i_maior)
		notas.pop(i_maior)

fim = time.perf_counter()

print(fim - inicio)
