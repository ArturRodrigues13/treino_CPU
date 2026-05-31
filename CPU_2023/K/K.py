import time

inicio = time.perf_counter()

while True:
	i, j = map(int, input().split(" "))

	if(i == 0 and j == 0):
		break

	print(2 * i - j)

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
