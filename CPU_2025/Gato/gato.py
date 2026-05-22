import time

inicio = time.perf_counter()

with open("Gato/entrada.txt","r") as file:
	conteudo = file.read().splitlines("")

casa = []
gato = []

casa = [int(item) for item in conteudo[0].split(" ")]
gato = [int(item) for item in conteudo[1].split(" ")]

if((gato[0] - casa[0])**2 + (gato[1] - casa[1])**2 <= casa[2]**2):
	print("Gato")
else:
	print("Gaiato")

fim = time.perf_counter()

print(fim - inicio)
