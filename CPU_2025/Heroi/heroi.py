import time

inicio = time.perf_counter()

with open("Heroi/entrada.txt","r") as file:
	conteudo = file.read().splitlines()

nome = conteudo[0].split(" ")
primeira_letra = nome[0][0]

aliterativo = True

for x in range(len(nome)):
	if not ((nome[x].startswith(primeira_letra))):
		aliterativo = False

if(aliterativo):
	print("Viva!")
else:
	print("Bah!")

fim = time.perf_counter()

print(fim - inicio)
