import time

inicio = time.perf_counter()

while True:
	try:
		movs = input()
		estado_atual = 0

		for x in range(len(movs)):
			m = movs[x]
			if(m == "E"):
				if(estado_atual == 0):
					estado_atual -= 1
					break

				estado_atual -= 1

			else:
				if(estado_atual == 10):
					break

				estado_atual += 1

		if(estado_atual == 0):
			print("S")
		else:
			print("N")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
