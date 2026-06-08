import time

inicio = time.perf_counter()

while True:
	try:
		linha = list(input())

		x = 0
		y = 0

		for i in range(len(linha)):
			if(linha[i] == "L"):
				x -= 1
			elif(linha[i] == "O"):
				x += 1
			elif(linha[i] == "S"):
				y += 1
			elif(linha[i] == "N"):
				y -= 1

		if(x == 0 and y == 0):
			print("Voltou")
		else:
			print("Deu zebra")

	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
