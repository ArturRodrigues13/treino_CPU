import time

inicio = time.perf_counter()

while True:
	try:

		mensagem, slop = input().split()
		caracteres = list(mensagem)
		achou = False

		i = 0
		ini = 0

		while True:

			procura = slop.find(caracteres[i],ini)
			if(procura != - 1):
				i += 1
				ini = procura + 1

				if i == len(caracteres):
					print("Jogou bonito")
					break
			else:
				print("Para com isso")
				break

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
