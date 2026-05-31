import time

inicio = time.perf_counter()

while True:

	p = int(input())

	if(p == 0):
		break

	predios = [int(item) for item in input().split(" ")]

	a_max = predios[0]

	quant = 1

	for x in range(p):
		if(predios[x] > a_max):
			quant +=1
			a_max = predios[x]


	print(quant)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
