import time

inicio = time.perf_counter()

with open("Jiu-Jitsu/entrada.txt","r") as file:
	conteudo = file.read().splitlines()

max = 0
min = 0
vitorias = 0
escolha1 = 0
escolha2 = 0

for x in range(len(conteudo)):
	jogadores = conteudo[x].split(" ")
	jogadores = [int(item) for item in jogadores]
	max = int(jogadores[0] / 2)
	min = 0
	vitorias = 0
	val = max
	jogadores.pop(0)

	for y in range(val):
		if(jogadores[max] > jogadores[min]):
			escolha1 = jogadores[max]
			jogadores.pop(max)
			max -=1
		elif(jogadores[min] > jogadores[max]):
			escolha1 = jogadores[min]
			jogadores.pop(min)
			max -=1

		if(jogadores[max] > jogadores[min]):
			escolha2 = jogadores[max]
			jogadores.pop(max)
			max -=1
		elif(jogadores[min] > jogadores[max]):
			escolha2 = jogadores[min]
			jogadores.pop(min)
			max -=1

		if(escolha1 > escolha2):
			vitorias += 1

	print(vitorias)



fim = time.perf_counter()

print(fim - inicio)
