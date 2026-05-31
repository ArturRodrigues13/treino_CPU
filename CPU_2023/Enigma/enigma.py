import time

inicio = time.perf_counter()

ida = ["z", "e", "n", "i", "t", "Z", "E", "N", "I", "T"]
volta = ["p", "o", "l", "a", "r", "P", "O", "L", "A", "R"]

while True:
	try:
		frase = list(input())

		for x in range(len(frase)):
			if(frase[x] in ida):

				ind = ida.index(frase[x])
				frase[x] = volta[ind]
				continue

			if(frase[x] in volta):
				ind = volta.index(frase[x])
				frase[x] = ida[ind]
				continue

		print("".join(frase))
	except EOFError:
		break

fim = time.perf_counter()

tempo = fim - inicio

if(tempo > 1.0):
	print(tempo)
