import time

inicio = time.perf_counter()

while True:

	try:

		n, capacidade = map(int, input().split())

		vetor = [int(item) for item in input().split()]

		vistos = set()
		achou = False

		for x in vetor:
			if(capacidade - x in vistos):
				achou = True
				break

			vistos.add(x)

		if(achou):
			print("SIM")
		else:
			print("NÃO")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
