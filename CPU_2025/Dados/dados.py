import time

inicio = time.perf_counter()

with open("Dados/entrada.txt","r") as file:
	conteudo = file.read().splitlines()

calcula = []
pontuacao = [0] * (int(conteudo[0]))
ganhadores = []
texto = ""

for x in range(int(conteudo[0])):
	texto = conteudo[x + 1]
	texto = texto.replace("(","")
	texto = texto.replace(")","")
	texto = texto.replace(","," ")
	texto = texto.split(" ")
	calcula = [int(item) for item in texto]

	for y in range(0, 10, 2) :
		if(calcula[y] == calcula[y+1]):
			pontuacao[x] += calcula[y] * calcula[y+1] * 2

		else:
			pontuacao[x] += calcula[y] * calcula[y+1]

for x in range(int(conteudo[0])):
	if(pontuacao[x]) == max(pontuacao):
		ganhadores.insert(1, x+1)

formata = ", ".join(str(num) for num in ganhadores)

print(f"Pontos do ganhador: {max(pontuacao)}")
print(f"Ganhador(es): " + formata)

fim = time.perf_counter()

print(fim - inicio)
