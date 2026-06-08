import time

inicio = time.perf_counter()

while True:

	try:

		n = int(input())

		baralho = [int(item) for item in input().split()]

		monte = [None]

		buscado = 1
		ind_b = 0
		max = 0

		while True:

			if(monte[max] != buscado):
				monte.append(baralho[ind_b])
				max += 1
				ind_b += 1
			else:
				monte.pop(max)
				max -= 1
				buscado += 1

			if(ind_b == len(baralho)):
				break

		for x in range(len(monte)):
			if(monte[max] == buscado):
				monte.pop(max)
				max -= 1
				buscado += 1
			else:
				break

		if(buscado == n + 1):
			print("SIM")
		else:
			print("NAO")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
