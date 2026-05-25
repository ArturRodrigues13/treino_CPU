import time

inicio = time.perf_counter()

jogadores = int(input())
calcula = []
pontuacao = []
ganhadores = []
texto = ""

for x in range(jogadores):
	pontuacao.append(0)
	texto = input()
	texto = texto.replace("(","")
	texto = texto.replace(")","")
	texto = texto.replace(","," ")
	texto = texto.split(" ")
	calcula = [int(item) for item in texto]

	for y in range(0, 10, 2) :

		if(calcula[y] == calcula[y+1] and calcula[y] == 1):
			pontuacao[x] += 30
			continue

		if(calcula[y] == calcula[y+1]):
			pontuacao[x] += calcula[y] * calcula[y+1] * 2
		else:
			pontuacao[x] += calcula[y] * calcula[y+1]

for x in range(jogadores):
	if(pontuacao[x]) == max(pontuacao):
		ganhadores.append(x + 1)

formata = ", ".join(str(num) for num in ganhadores)

print(f"Pontos do ganhador: {max(pontuacao)}")
print(f"Ganhador(es): " + formata)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
