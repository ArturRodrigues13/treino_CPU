import time

inicio = time.perf_counter()

maximo = int(input())
estacionamento = []
espera = []

while True:

	try:

		placa, op = input().split()
		mudanca = False

		if(op == "E"):
			if(len(estacionamento) < maximo):
				estacionamento.append(placa)
				mudanca = True
			else:
				espera.append(placa)

		else:

			if(placa in estacionamento):
				index = estacionamento.index(placa)
				estacionamento = estacionamento[index + 1:] + estacionamento[:index]
				mudanca = True
				if(len(espera) > 0):
					estacionamento.append(espera.pop(0))
					mudanca = True
			else:
				index = espera.index(placa)
				espera.pop(index)

		if(mudanca):
			if(len(estacionamento) > 0):
				print(" ".join(estacionamento),end="")

			else:
				print("VAZIA", end="")

			print()

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
