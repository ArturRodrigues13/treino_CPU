import time

inicio = time.perf_counter()

with open("entrada.txt","r") as file:
	conteudo = file.read().splitlines()

valores_linha1 = conteudo[0].split(" ")
valores_linha2 = conteudo[1].split(" ")
val1 = 0
val2 = 0

for x in range(int(valores_linha1[0])):
	valores_linha1[x + 1] = int(valores_linha1[x + 1])
	val1 += valores_linha1[x + 1]

for x in range(int(valores_linha2[0])):
	valores_linha2[x + 1] = int(valores_linha2[x + 1])
	val2 += valores_linha2[x + 1]

if(val1 == val2):
	print("OK")
elif(val1 > val2):
	val1 -= val2
	print(f"E > D: {val1} kg")
elif(val2 > val1):
	val2 -= val1
	print(f"E > D: {val2} kg")

fim = time.perf_counter()

print(fim - inicio)
